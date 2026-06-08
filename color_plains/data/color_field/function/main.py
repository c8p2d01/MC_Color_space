import variables as var
import color_conversion as colmath
import mc_writer
from datapack_logic import generate_logic
import texture_analysis as tsys
import numpy as np
import pandas as pd
import ast
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

    def get_base(name:str):
        name = name.removesuffix(".png")
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
    
    names = [f.name for f in Path(var.texture_folder + "block/").iterdir() if f.is_file() and f.name.endswith(".png")]

    blocks = defaultdict(list)

    for f in names:
        base = get_base(f)

        blocks[base].append(f)

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
                f.write(mc_writer.create_summon_string_block(x * var.CUBE_SIZE, 0, z * var.CUBE_SIZE, "minecraft:" + items[index], "all_blocks", var.CUBE_SIZE))
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

def generate_summons(data):
    groups = data["category"].unique()
    rgb_files = {}
    hsl_files = {}
    lab_files = {}
    oklab_files = {}
    oklch_files = {}
    for g in groups:
        rgb_files[g] = open(f"{var.SCRIPT_DIR}/render/blocks/rgb/{g}.mcfunction", "w+")
        hsl_files[g] = open(f"{var.SCRIPT_DIR}/render/blocks/hsl/{g}.mcfunction", "w+")
        lab_files[g] = open(f"{var.SCRIPT_DIR}/render/blocks/lab/{g}.mcfunction", "w+")
        oklab_files[g] = open(f"{var.SCRIPT_DIR}/render/blocks/oklab/{g}.mcfunction", "w+")
        oklch_files[g] = open(f"{var.SCRIPT_DIR}/render/blocks/oklch/{g}.mcfunction", "w+")

    for index, row in data.iterrows():
        block_id = row['Key']
        texture_list = ast.literal_eval(row['Items'])
        group = row['category']
        
        display_positions = tsys.find_positions(texture_list)

        for p in display_positions:
             x,y,z = colmath.rgb_to_rgb(p[0], p[1], p[2])
             rgb_files[group].write(mc_writer.create_summon_string_block(x, y, z, block_id, group))
             x,y,z = colmath.xyz_to_hsl(p[0], p[1], p[2])
             hsl_files[group].write(mc_writer.create_summon_string_block(x, y, z, block_id, group))
             x,y,z = colmath.xyz_to_lab(p[0], p[1], p[2])
             lab_files[group].write(mc_writer.create_summon_string_block(x, y, z, block_id, group))
             x,y,z = colmath.xyz_to_oklab(p[0], p[1], p[2])
             oklab_files[group].write(mc_writer.create_summon_string_block(x, y, z, block_id, group))
             x,y,z = colmath.xyz_to_oklch(p[0], p[1], p[2])
             oklch_files[group].write(mc_writer.create_summon_string_block(x, y, z, block_id, group))
    
    for g in groups:
        rgb_files[g].close()
        hsl_files[g].close()
        lab_files[g].close()
        oklab_files[g].close()
        oklch_files[g].close()

if __name__ == "__main__":
    try:
        var.validate_folders()
    except Exception as e:
        print(f"Error: {e}\nplease provide the path to the texture folder in variables.py")
        exit(127)
    mc_writer.create_ui_markers(f"{var.SCRIPT_DIR}/ui/sphere_markers.mcfunction")

    blocks =  list_textures()

    # test_summon(blocks)

    data = frame_blocks(blocks)

    generate_logic(data)
    
    try:
        generate_summons(data)
    except Exception as e:
        print(f"Error: {e}\n")

    pass
