import variables as var
import color_conversion as colmath
import mc_writer
import csv
import numpy as np
import pandas as pd
import ast
import shutil
from PIL import Image
from pathlib import Path
from collections import defaultdict

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

try:
    from pyclustering.cluster.clique import clique
    CLIQUE_AVAILABLE = True
except ImportError:
    CLIQUE_AVAILABLE = False

def list_textures():
    SUFFIXES = {
        "top",
        "open",
        "bottom",
        "side",
        "small",
        "side0",
        "side1",
        "side2",
        "side3",
        "side4",
        "front",
        "on",
        "off",
        "honey",
        "end",
        "back",
        "inner",
        "outer",
        "stalk",
        "stage", # only pitcher_crop
        "stage0", # plant variants
        "stage1",
        "stage2",
        "stage3",
        "stage4",
        "stage5",
        "stage6",
        "stage7",
        "powered",
        "flow",
        "still",
        "head",# beds
        "foot",
        "east",
        "south",
        "west",
        "up",
        "north", # north only for crafter ?
        "down",
        "ominous",
        "ejecting",
        "slightly",
        "tall",
        "lit",
        "particle",
        "0", # suspicious variants, ghast variants?
        "1",
        "2",
        "3", 
        "4",
        "tip",# dripleaf , pointy dripstone
        "input",
        "empty", # chisledbookshelf
        "occupied",
        "dead",
        "conditional",
        "compost",
        "ready",
        "crafting",
        "triggered",
        "awake", # creaking_heart
        "dormant",
        "inverted",
        "base",
        "vertical",
        "hydration",
        "tentacles",
        "moist",
        "emissive",
        "overlay",
        "pivot", #grindstone
        "round",
        "inside", # hopper
        "outside",
        "lock", #jigsaw structure block
        "data",
        "load",
        "save",
        "sticky",
        "frustum",
        "middle",
        "merge",
        "plant", # pottet azelea comes with pot texture ?
        "crop",
        "pot",
        "corner",
        "dot",
        "line0",
        "line1",
        "active",
        "inactive",
        "tendrill",
        "cracked",
        "not",
        "slightly",
        "very",
        "saw",
        "ejecting",
        "reward",
        "eye",
    }
    SPECIAL_SUFFIXES = ( # Suffixes that apply to block ids longer than 2 words
        "stem", # for big_dripleaf, but not crimson and warped
        "snow", # for grass_block, but not powder
        "amethyst",
    )
    PREFIXES = (
        "attached",
    )

    def get_base(name):
        parts = name.split("_")

        # remove suffixes from the end
        if (parts[0] == "destroy" or parts[0] == "test" or parts[0] == "debug" or parts[0] == "debug2"):
            return ("")
        while len(parts) > 2 and parts[-1] in SPECIAL_SUFFIXES:
            parts.pop()
        while len(parts) > 1 and parts[-1] in SUFFIXES:
            parts.pop()
        while len(parts) > 1 and parts[0] in PREFIXES:
            parts.pop(0)

        joined = "_".join(parts)
        #edge cases
        if (joined == "campfire_fire" or joined == "campfire_log"):
            return ("campfire")
        if (joined == "wildflowers_stem"):
            return ("wildflowers")
        if (joined == "dried_kelp"):
            return ("dried_kelp_block")
        if (joined == "flower"):
            return ("flower_pot")
        if (joined == "chorus"):
            return ("chorus_plant")
        if (joined == "glow_item_frame"):
            return ("")
        if (joined == "bamboo_large_leaves" or joined == "bamboo_small_leaves" or joined == "bamboo_singleleaf"):
            return ("bamboo")
        return (joined)
    
    files = [f.name for f in Path(var.texture_folder).iterdir() if f.is_file()]
    names = []

    for f in files:
        stems = f.split(".")
        if (stems[-1] == "mcmeta"):
            continue
        if (stems[-1] == "png"):
            stems.pop()
        names.append(".".join(stems))
    
    blocks = defaultdict(list)

    for f in names:
        base = get_base(f)

        blocks[base].append(f + ".png")

    # for k, v in blocks.items():
    #     print(f"{k}:")
    return dict(blocks)

def test_summon(blocks):
    f = open(str(var.SCRIPT_DIR) + "/test_summon_all.mcfunction", "w+")
    index = 0
    items = list(blocks.keys())
    for x in range(16):
        for z in range(20):
            if (index < len(items)):
                f.write(mc_writer.create_summon_string(x * var.CUBE_SIZE, 0, z * var.CUBE_SIZE, "minecraft:" + items[index], "all_blocks", var.CUBE_SIZE))
            index += 1

def classify_blocks(row):
    key_text = row['Key']
    
    # Komplexe Bedingungen basierend auf dem Text im Key
    if "leaves" in key_text or "dark_oak" in key_text or "oak" in key_text or "birch" in key_text or "cherry" in key_text \
        or "crimson" in key_text or "warped" in key_text or "acacia" in key_text or "azalea" in key_text \
        or "jungle" in key_text or "spruce" in key_text or "mangrove" in key_text or "bamboo" in key_text:
        return "wood"
    elif "wool" in key_text or "bed" in key_text:
        return "wool"
    elif "_powder" in key_text:
        return "concrete_powder"
    elif "concrete" in key_text:
        return "concrete"
    elif "terracotta" in key_text:
        return "terracotta"
    elif "glass" in key_text:
        return "glass"
    elif "sculk" in key_text:
        return "sculk"
    elif "candle" in key_text or "froglight" in key_text or "shroomlight" in key_text or "soul" in key_text or "campfire" in key_text or "lantern" in key_text:
        return "light"
    elif "coral" in key_text:
        return "coral"
    elif "dirt" in key_text or "grass" in key_text or "mycelium" in key_text or "clay" in key_text or "gravel" in key_text or "sand" == key_text:
        return "dirt"
    elif "bedrock" in key_text or "command" in key_text or "spawner" in key_text or "vault" in key_text:
        return "creative"
    elif "stone" in key_text or "tuff" in key_text or "chiseled" in key_text or "basalt" in key_text or "bricks" in key_text \
        or "tiles" in key_text or "resin" in key_text or "calcite" in key_text or "andesite" in key_text or "diorite" in key_text or "granite" in key_text:
        return "stone"
    elif "melon" in key_text or "pumpkin" in key_text:
        return "crops"
    elif "barrel" in key_text or "bee" in key_text or "bee" in key_text or "smoker" in key_text or "cauldron" in key_text \
        or "brewing" in key_text or "bookshelf" in key_text or "shulker" in key_text or "bell" in key_text or "rail" in key_text \
        or "anvil" in key_text or "furnace" in key_text:
        return "utility"
    elif "amethyst" in key_text or "ore" in key_text or "weathered" in key_text or "copper" in key_text or "coal" in key_text \
        or "iron" in key_text or "gold" in key_text or "lapis" in key_text or "redstone" in key_text or "diamond" in key_text:
        return "ore"
    elif "ice" in key_text or "snow" in key_text:
        return "ice"
    elif "block" in key_text:
        return "block"
    elif "bricks" in key_text:
        return "stone"
    else:
        return "misc"

def frame_blocks(blocks):
    df = pd.DataFrame([{"Key": k, "Items": str(v)} for k, v in blocks.items()])
    df['category'] = df.apply(classify_blocks, axis=1)
    return df

def generate_logic(data):
    groups = data["category"].unique()
    layer = 4
    angle = 330
    shutil.copy2(f"{var.SCRIPT_DIR}/load_template", f"{var.SCRIPT_DIR}/load.mcfunction")
    load = open(f"{var.SCRIPT_DIR}/load.mcfunction", "a+")
    shutil.copy2(f"{var.SCRIPT_DIR}/tick_template", f"{var.SCRIPT_DIR}/tick.mcfunction")
    tick = open(f"{var.SCRIPT_DIR}/tick.mcfunction", "a+")
    shutil.copy2(f"{var.SCRIPT_DIR}/ui/build_ui_template", f"{var.SCRIPT_DIR}/ui/build_ui.mcfunction")
    build = open(f"{var.SCRIPT_DIR}/ui/build_ui.mcfunction", "a+")
    shutil.copy2(f"{var.SCRIPT_DIR}/ui/click_template", f"{var.SCRIPT_DIR}/ui/click.mcfunction")
    clck = open(f"{var.SCRIPT_DIR}/ui/click.mcfunction", "a+")
    shutil.copy2(f"{var.SCRIPT_DIR}/render/render_template", f"{var.SCRIPT_DIR}/render/render.mcfunction")
    render = open(f"{var.SCRIPT_DIR}/render/render.mcfunction", "a+")
    for g in groups:
        load.write(f"scoreboard objectives add cf_block_{g} dummy\n")
        load.write(f"execute as @p run scoreboard players set @s cf_block_{g} 0\n")
        clck.write(f"execute if entity @s[tag=toggle_{g}] if data entity @s interaction.player on target run function color_field:ui/logics/_{g}\n")
        build.write(f"function color_field:ui/elements/_{g}\n")
        render.write(mc_writer.create_render_logic(g))
        e = open(f"{var.SCRIPT_DIR}/ui/elements/_{g}.mcfunction", "w+")
        e.write(mc_writer.create_ui_element(g, layer, angle))
        e.close()
        f = open(f"{var.SCRIPT_DIR}/ui/logics/_{g}.mcfunction", "w+")
        f.write(mc_writer.create_ui_logic(g))
        f.close()
        layer -= 1
        if (layer < 0):
            layer = 4
            angle -= 15
    render.write(f"execute as @e[tag=color_field_anchor,limit=1] at @s run summon interaction ~ ~ ~ "\
                 f"{{Tags:[\"color_field\",\"block_shifter\"],width:{var.CUBE_SIZE / 32}f,"\
                 f"height:{var.CUBE_SIZE / 32}f}}\n"\
                 f"\n"\
                 f"execute store result score #count cf_counter_node if score @s cf_coltype matches 0..7 run execute if entity @e[type=text_display,tag=color_field_node]\n"\
                 f"\n"\
                 f"execute store result score #count cf_counter_node if score @s cf_coltype matches 8..15 run execute if entity @e[type=block_display,tag=color_field_block]\n"\
                 f"\n"\
                 f"execute if score @s cf_feedback matches 1 run tellraw @a [{{\"text\":\"[ColorField] \",\"color\":\"dark_aqua\",\"bold\":true}},"\
                 f"{{\"text\":\"Number of active Nodes\",\"color\":\"green\"}},{{\"score\":{{\"name\":\"#count\",\"objective\":\"cf_counter_node\"}},\"color\":\"gold\",\"bold\":true}}]\n"
                )

    tick.write(f"execute as @e[tag=block_shifter] at @s if entity @p[distance=..5,limit=1] run "\
                 f"tp @s ~{var.CUBE_SIZE / 64} ~ ~{var.CUBE_SIZE / 64}")
    clck.write("\ndata remove entity @s interaction\n")

def load_png_pixel_data(path):
    image = Image.open(path).convert('RGB')
    return np.array(image)

def rgb_to_3d_points(pixel_array, normalize=True, scale=1.0):
    if pixel_array.ndim != 3 or pixel_array.shape[2] != 3:
        raise ValueError('Expected RGB pixel array with shape (H, W, 3)')
    points = pixel_array.reshape((-1, 3)).astype(np.float64)
    if normalize:
        points /= 255.0
    points *= scale
    return points

def estimate_k(points, k_min=2, k_max=12):
    unique_point_count = len(np.unique(points, axis=0))

    k_max = min(k_max, unique_point_count)

    if k_max < k_min:
        return k_max

    best_k = k_min
    best_score = -1

    for k in range(k_min, k_max + 1):
        model = KMeans(n_clusters=k, n_init='auto', random_state=42)
        labels = model.fit_predict(points)

        if len(np.unique(labels)) < 2:
            continue

        score = silhouette_score(points, labels)

        if score > best_score:
            best_score = score
            best_k = k

    return best_k

def cluster_points(points, min_cluster_size=10, k=None):
    unique_point_count = len(np.unique(points, axis=0))
    if k is None:
        k = estimate_k(points)
    k = min(k, unique_point_count)

    model = KMeans(n_clusters=k, n_init='auto', random_state=42)
    labels = model.fit_predict(points)

    unique_labels, counts = np.unique(labels, return_counts=True)

    valid_clusters = unique_labels[counts >= min_cluster_size]

    mask = np.isin(labels, valid_clusters)

    filtered_points = points[mask]
    filtered_labels = labels[mask]

    return filtered_points, filtered_labels, k

def compute_cluster_means(points, labels):
    unique_labels = np.unique(labels)

    means = []

    for label in unique_labels:
        cluster_points = points[labels == label]
        mean_point = cluster_points.mean(axis=0)
        means.append(mean_point)

    return np.array(means)

def merge_close_midpoints(midpoints, threshold=0.1):
    if len(midpoints) <= 1:
        return midpoints
    
    merged = []
    used = set()
    
    for i, mp1 in enumerate(midpoints):
        if i in used:
            continue
        current_cluster = [mp1]
        for j, mp2 in enumerate(midpoints):
            if i != j and j not in used:
                dist = np.linalg.norm(np.array(mp1) - np.array(mp2))
                if dist < threshold:
                    current_cluster.append(mp2)
                    used.add(j)
        
        merged.append(np.mean(current_cluster, axis=0).tolist())
        used.add(i)
        
    return merged

def find_positions(texture_list):
    midpoints = []
    points = []
    for texture in texture_list:
        try:
            pixs = load_png_pixel_data(var.texture_folder + texture)
            pts = rgb_to_3d_points(pixs, normalize=True, scale=1.0)
            points.append(pts)
          #  break  this is effectively only checking the first texture
        except Exception as e:
            print(f"errrrrrrr{e}")
    if points:
        combined_points = np.concatenate(points, axis=0)
        filtered_points, labels, k = cluster_points(
            combined_points,
            min_cluster_size=25
        )
        unique_labels = np.unique(labels)
        midpoints = compute_cluster_means(filtered_points, labels)
        return (merge_close_midpoints(midpoints))
    return ([])

def generate_summons(data):
    groups = data["category"].unique()
    rgb_files = {}
    hsl_files = {}
    lab_files = {}
    oklab_files = {}
    oklch_files = {}
    for g in groups:
        r = open(f"{var.SCRIPT_DIR}/render/blocks/rgb/{g}.mcfunction", "w+")
        rgb_files[g] = r
        h = open(f"{var.SCRIPT_DIR}/render/blocks/hsl/{g}.mcfunction", "w+")
        hsl_files[g] = h
        l = open(f"{var.SCRIPT_DIR}/render/blocks/lab/{g}.mcfunction", "w+")
        lab_files[g] = l
        a = open(f"{var.SCRIPT_DIR}/render/blocks/oklab/{g}.mcfunction", "w+")
        oklab_files[g] = a
        c = open(f"{var.SCRIPT_DIR}/render/blocks/oklch/{g}.mcfunction", "w+")
        oklch_files[g] = c

    for index, row in data.iterrows():
        block_id = row['Key']
        texture_list = ast.literal_eval(row['Items'])
        group = row['category']
        
        # print(texture_list[0])
        display_positions = find_positions(texture_list)

        for p in display_positions:
             x,y,z = colmath.rgb_to_rgb(p[0], p[1], p[2])
             rgb_files[group].write(mc_writer.create_summon_string(x, y, z, block_id, group))
             x,y,z = colmath.rgb_to_hsl(p[0], p[1], p[2])
             hsl_files[group].write(mc_writer.create_summon_string(x, y, z, block_id, group))
             x,y,z = colmath.rgb_to_lab(p[0], p[1], p[2])
             lab_files[group].write(mc_writer.create_summon_string(x, y, z, block_id, group))
             x,y,z = colmath.rgb_to_oklab(p[0], p[1], p[2])
             oklab_files[group].write(mc_writer.create_summon_string(x, y, z, block_id, group))
             x,y,z = colmath.rgb_to_oklch(p[0], p[1], p[2])
             oklch_files[group].write(mc_writer.create_summon_string(x, y, z, block_id, group))
    
    for g in groups:
        rgb_files[g].close()
        hsl_files[g].close()
        lab_files[g].close()
        oklab_files[g].close()
        oklch_files[g].close()



if __name__ == "__main__":
    # iterate_textures()
    try:
        blocks =  list_textures()
    except Exception as e:
        print(f"Error: {e}\nprobably failed to load textures.\nplease provide the path to the texture folder in variables.py")

    # test_summon(blocks)

    data = frame_blocks(blocks)

    generate_logic(data)
    
    # try:
    generate_summons(data)
    # except Exception as e:
        # print(f"Error: {e}\n")

    pass
