import csv
import numpy as np
import pandas as pd
import ast
import shutil
from PIL import Image
from pathlib import Path
from collections import defaultdict
try:
    from pyclustering.cluster.clique import clique
    CLIQUE_AVAILABLE = True
except ImportError:
    CLIQUE_AVAILABLE = False

# Gets the directory where the current script lives
SCRIPT_DIR = Path(__file__).resolve().parent
CUBE_SIZE = 4
RESOLUTION = 16
HALF = CUBE_SIZE / 2
texture_folder = f""

def create_ui_element(group, pos_layer, pos_angle):
    return (
        f"execute if score @s cf_block_{group} matches 1 as @e[type=interaction,tag=layer_{pos_layer},tag=yawstep_{pos_angle}] at @s run "\
        f"summon text_display ^ ^ ^ {{"\
        f"Tags:[\"color_field\",\"color_field_ui\",\"ui_block_{group}\"],"\
        f"text:{{\"text\":\"{group}\",\"color\":\"green\"}},"\
        f"billboard:\"center\","\
        f"brightness:{{block:15,sky:15}},"\
        f"transformation:{{"\
            f"translation:[0f,0f,0f],"\
            f"left_rotation:[0f,0f,0f,1f],"\
            f"right_rotation:[0f,0f,0f,1f],"\
            f"scale:[1.0f,1.0f,1.0f]"\
        f"}}"\
        f"}}\n"\
        f"execute unless score @s cf_block_{group} matches 1 as @e[type=interaction,tag=layer_{pos_layer},tag=yawstep_{pos_angle}] at @s run "\
            f"summon text_display ^ ^ ^ {{"\
            f"Tags:[\"color_field\",\"color_field_ui\",\"ui_block_{group}\"],"\
            f"text:{{\"text\":\"{group}\",\"color\":\"dark_gray\"}},"\
            f"billboard:\"center\","\
            f"brightness:{{block:15,sky:15}},"\
            f"transformation:{{"\
                f"translation:[0f,0f,0f],"\
                f"left_rotation:[0f,0f,0f,1f],"\
                f"right_rotation:[0f,0f,0f,1f],"\
                f"scale:[1.0f,1.0f,1.0f]"\
            f"}}"\
        f"}}\n\n"\
        f"tag @e[type=interaction,tag=layer_{pos_layer},tag=yawstep_{pos_angle},limit=1] add toggle_{group}"
    )

def create_summon_string(x, y, z, block, group, scale_divisor=32):
    return (\
        f"execute as @e[tag=color_field_anchor,limit=1] at @s run summon block_display "\
        f"~{(x * CUBE_SIZE - CUBE_SIZE / 2):.4f} ~{(y * CUBE_SIZE - CUBE_SIZE / 2):.4f} ~{(z * CUBE_SIZE - CUBE_SIZE / 2):.4f} {{"\
        f"Tags:[\"color_field\",\"color_field_block\",\"render_{group}\"],"\
        f"block_state:{{Name:\"{block}\"}},"\
        f"brightness:{{block:15,sky:15}},"\
        f"transformation:{{"\
        f"translation:[0f,0f,0f],"\
        f"left_rotation:[0f,0f,0f,1f],"\
        f"right_rotation:[0f,0f,0f,1f],"\
        f"scale:[{CUBE_SIZE / scale_divisor}f,{CUBE_SIZE / scale_divisor}f,{CUBE_SIZE / scale_divisor}f]"\
        f"}}"\
        f"}}\n"\
    )

def create_ui_logic(group):
    return (
        f"execute if score @s cf_block_{group} matches 1 run scoreboard players set @s cf_block_{group} 2\n"\
        f"execute unless score @s cf_block_{group} matches 1..2 run scoreboard players set @s cf_block_{group} 1\n"\
        f"execute if score @s cf_block_{group} matches 2 run scoreboard players set @s cf_block_{group} 0\n"\
        f"# kill @e[type=text_display,tag=\"ui_block_{group}\"]\n"\
        f"# function color_field:ui/elements/_{group}\n"\
        f"function color_field:render/blocks/set"\
    )

def create_render_logic(group):
    return (\
        f"# {group}\n"\
        f"execute \\\n"\
        f"if score @s cf_coltype matches 8 \\\n"\
        f"if score @s cf_block_{group} matches 1 \\\n"\
        f"run function color_field:render/blocks/{group}\n\n"\
    )

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
    
    files = [f.name for f in Path(texture_folder).iterdir() if f.is_file()]
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
    f = open(str(SCRIPT_DIR) + "/test_summon_all.mcfunction", "w+")
    index = 0
    items = list(blocks.keys())
    for x in range(16):
        for z in range(20):
            if (index < len(items)):
                f.write(create_summon_string(x * CUBE_SIZE, 0, z * CUBE_SIZE, "minecraft:" + items[index], "all_blocks", CUBE_SIZE))
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
    shutil.copy2(f"{SCRIPT_DIR}/load_template", f"{SCRIPT_DIR}/load.mcfunction")
    load = open(f"{SCRIPT_DIR}/load.mcfunction", "a+")
    shutil.copy2(f"{SCRIPT_DIR}/tick_template", f"{SCRIPT_DIR}/tick.mcfunction")
    tick = open(f"{SCRIPT_DIR}/tick.mcfunction", "a+")
    shutil.copy2(f"{SCRIPT_DIR}/ui/build_ui_template", f"{SCRIPT_DIR}/ui/build_ui.mcfunction")
    build = open(f"{SCRIPT_DIR}/ui/build_ui.mcfunction", "a+")
    shutil.copy2(f"{SCRIPT_DIR}/ui/click_template", f"{SCRIPT_DIR}/ui/click.mcfunction")
    clck = open(f"{SCRIPT_DIR}/ui/click.mcfunction", "a+")
    shutil.copy2(f"{SCRIPT_DIR}/render/render_template", f"{SCRIPT_DIR}/render/render.mcfunction")
    render = open(f"{SCRIPT_DIR}/render/render.mcfunction", "a+")
    for g in groups:
        load.write(f"scoreboard objectives add cf_block_{g} dummy\n")
        load.write(f"execute as @p run scoreboard players set @s cf_block_{g} 0\n")
        clck.write(f"execute if entity @s[tag=toggle_{g}] if data entity @s interaction.player on target run function color_field:ui/logics/_{g}\n")
        build.write(f"function color_field:ui/elements/_{g}\n")
        render.write(create_render_logic(g))
        e = open(f"{SCRIPT_DIR}/ui/elements/_{g}.mcfunction", "w+")
        e.write(create_ui_element(g, layer, angle))
        e.close()
        f = open(f"{SCRIPT_DIR}/ui/logics/_{g}.mcfunction", "w+")
        f.write(create_ui_logic(g))
        f.close()
        layer -= 1
        if (layer < 0):
            layer = 4
            angle -= 15
    render.write(f"execute as @e[tag=color_field_anchor,limit=1] at @s run summon interaction ~ ~ ~ "\
                 f"{{Tags:[\"color_field\",\"block_shifter\"],width:{CUBE_SIZE / 32}f,"\
                 f"height:{CUBE_SIZE / 32}f}}")
    tick.write(f"execute as @e[tag=block_shifter] at @s if entity @p[distance=..5,limit=1] run "\
                 f"tp @s ~{CUBE_SIZE / 64} ~ ~{CUBE_SIZE / 64}")
    clck.write("\ndata remove entity @s interaction\n")

def load_png_pixel_data(path):
    image = Image.open(path).convert('RGB')
    pixels = np.array(image)
    return pixels

def rgb_to_3d_points(pixel_array, normalize=True, scale=1.0):
    if pixel_array.ndim != 3 or pixel_array.shape[2] != 3:
        raise ValueError('Expected RGB pixel array with shape (H, W, 3)')
    height, width, _ = pixel_array.shape
    points = pixel_array.reshape((-1, 3)).astype(np.float64)
    if normalize:
        points /= 255.0
    points *= scale
    return points

def cluster_points(points, **kwargs):
    
    if not CLIQUE_AVAILABLE:
        raise ImportError('pyclustering library is not installed. Install with: pip install pyclustering')
    intervals = kwargs.get('intervals', 5)  
    density_threshold = kwargs.get('density_threshold', 5)
    model = clique(points, intervals, density_threshold)
    model.process()
    clusters = model.get_clusters()
    labels = np.full(len(points), -1, dtype=int)
    for cluster_id, cluster_indices in enumerate(clusters):
        labels[cluster_indices] = cluster_id
    return labels

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
            pixs = load_png_pixel_data(texture_folder + texture)
            pts = rgb_to_3d_points(pixs, normalize=True, scale=1.0)
            points.append(pts)
            break
        except Exception as e:
            print(f"{e}")
    if points:
        combined_points = np.concatenate(points, axis=0)
        labels = cluster_points(combined_points)
        unique_labels = np.unique(labels)
        noise_points = []
        for label in unique_labels:
            if label == -1:
                continue
            
            cluster_pts = combined_points[labels == label]
            if (len(cluster_pts) < len(combined_points) / 4):
                noise_points.append(cluster_pts)
                continue
            
            midpoint = np.mean(cluster_pts, axis=0)
            midpoints.append(midpoint.tolist())
        if (len(noise_points) > len(combined_points) / 4):
            all_noise = np.concatenate(noise_points, axis=0)
            midpoint = np.mean(all_noise, axis=0)
            midpoints.append(midpoint.tolist())
        return (merge_close_midpoints(midpoints))
    return ([])

def iterate_textures():
    input_file = "full_blocks.csv"
    output_file = "full_blocks_rgb_positions.csv"

    # Name der neuen Spalte
    coordinate_column = "coordinates"
    try:
        with open(str(SCRIPT_DIR) + "/" + input_file, mode="r+", encoding="utf-8") as infile:
            reader = csv.reader(infile, delimiter=";", quotechar='"')
            rows = list(reader)


            sets = set()
            for row in rows[1:]:
                if len(row) < 3:
                    continue

                block_id = row[1]
                texture_list = row[2].split()

                result = find_positions(texture_list)

                row.append(result)
                sets.add(row[0])
            
            print(sets)

            files = {}
            for s in sets:
                f = open(f"{SCRIPT_DIR}/summoners/{s.lower()}.mcfunction", "w+")
                files[s] = f

            for row in rows[1:]:
                if len(row) < 3:
                    continue
                for p in row[3]:
                    files[row[0]].write(create_summon_string(p[0], p[1], p[2], row[1], row[0]))

            
            
        print(f"Erfolgreich! Die neue Datei wurde als '{output_file}' gespeichert.")

    except Exception as e:
        print(f"Fehler bei {e}")

def generate_summons(data):
    groups = data["category"].unique()
    files = {}
    for g in groups:
        f = open(f"{SCRIPT_DIR}/render/blocks/{g}.mcfunction", "w+")
        files[g] = f

    for index, row in data.iterrows():
        block_id = row['Key']
        texture_list = ast.literal_eval(row['Items'])
        group = row['category']
        
        # print(texture_list[0])
        display_positions = find_positions(texture_list)

        for p in display_positions:
             files[group].write(create_summon_string(p[0], p[1], p[2], block_id, group))



if __name__ == "__main__":
    # iterate_textures()
    blocks =  list_textures()
    # test_summon(blocks)
    data = frame_blocks(blocks)

    generate_logic(data)
    generate_summons(data)

    pass
