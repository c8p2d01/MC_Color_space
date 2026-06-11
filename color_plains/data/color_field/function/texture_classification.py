import MC_Color_space.color_plains.data.color_field.function.variables as var
import MC_Color_space.color_plains.data.color_field.function.mc_writer as mc_writer
from MC_Color_space.color_plains.data.color_field.function.block_class import Block
from MC_Color_space.color_plains.data.color_field.function.block_class import BlockVariant
import json
import numpy as np
from tqdm import tqdm
from PIL import Image
import matplotlib.pyplot as plt
from pathlib import Path
from collections import defaultdict
import re

def trim_filetype(name):
    parts = name.split(".")
    if len(parts) > 1:
        parts.pop()
    joined = ".".join(parts)
    return (joined)

def prepend_model_path(parent):
    return f"{var.model_folder}{parent.replace('minecraft:', '')}"

def prepend_texture_path(texture):
    return f"{var.texture_folder}{texture.replace('minecraft:', '')}.png"

def prepend_state_path(texture):
    return f"{var.block_state_folder}{texture.replace('minecraft:', '')}"

def list_block_models() -> defaultdict[str, list[str]]:
    """
    iterate through all block states and list all unique models found within
    """
    key = {}
    if Path(var.block_state_folder).is_dir():
        for file_path in Path(var.block_state_folder).iterdir():
            if file_path.is_file() and file_path.suffix == '.json':
                with open(file_path, "r", encoding="utf-8") as file:
                    try:
                        info = json.load(file)
                        if not info:
                            continue

                        file_name = file_path.name

                        if "variants" in info:
                            variants = info["variants"]
                            for k, v in variants.items():
                                v_list = v if isinstance(v, list) else [v]
                                for variant_entry in v_list:
                                    if isinstance(variant_entry, dict):
                                        model_name = variant_entry.get("model")
                                        model = prepend_model_path(model_name) + ".json"
                                        if model:
                                            if file_name not in key:
                                                key[file_name] = []
                                            if model not in key[file_name]:
                                                key[file_name].append(model)

                        elif "multipart" in info:
                            multipart = info["multipart"]
                            for part in multipart:
                                if isinstance(part, dict) and "apply" in part:
                                    apply_value = part["apply"]
                                    apply_list = apply_value if isinstance(apply_value, list) else [apply_value]

                                    for apply_entry in apply_list:
                                        if isinstance(apply_entry, dict):
                                            model_name = apply_entry.get("model")
                                            model = prepend_model_path(model_name) + ".json"
                                            if model:
                                                if file_name not in key:
                                                    key[file_name] = []
                                                if model not in key[file_name]:
                                                    key[file_name].append(model)

                    except json.JSONDecodeError:
                        print(f"Error! couldnt read this file : {file_path.name}")

    file = open(f"{var.SCRIPT_DIR}/info/all_models.txt", "w+", encoding="utf-8")
    for k,v in key.items():
        for m in v:
            file.write(f"{m}\n")
    file.close()

    return (key)

def open_texture(image_path: str) -> np.ndarray:
    pixels = []
    if image_path.endswith(".png"):
        img = Image.open(image_path)
        img = img.convert("RGBA")
        pixels = np.array(img)
        img.close()
    return pixels

def display_texture(img: np.ndarray):
    """Display an image array in a new matplotlib window."""

    def on_key(event):
        if event.key == "escape":
            plt.close("all")

    try:
        plt.imshow(img, cmap="gray")

        plt.axis("on")

        fig = plt.gcf()
        fig.canvas.mpl_connect("key_press_event", on_key)

        plt.show()

    except KeyboardInterrupt:
        plt.close("all")
        return
    
def save_texture(img: np.ndarray, path: str):
    """Speichert ein Bild-Array als Datei ab, statt es anzuzeigen."""
    try:
        plt.imshow(img, cmap="gray")
        plt.axis("on")

        plt.savefig(path, bbox_inches="tight", dpi=300)

    except Exception as e:
        print(f"Error storing in {path}: {e}")
    finally:
        plt.close("all")

def recurse_texture_resolve(model: BlockVariant, model_path: str):

    try:
        with open(model_path, 'r', encoding='utf-8') as file:
            info = json.load(file)
    except Exception as e:
        print(f"opening issue: {model_path} ({e})")
        return

    name = trim_filetype(model_path)
    parent = info.get("parent")
    if parent:
        parent = prepend_model_path(parent)
        if parent != name:
            recurse_texture_resolve(model, f"{parent}.json")


    for field in info:
        if field not in model.fields or not model.fields[field]:
            model[field] = info[field]
        elif isinstance(model[field], dict) and isinstance(info[field], dict):
            merged_dict = model[field].copy()
            for k, v in info[field].items():
                merged_dict[k] = v
            model[field] = merged_dict
        elif isinstance(model[field], list) and isinstance(info[field], list):
            model[field] = info[field]
        else:
            model[field] = info[field]

def texture_block_from_model(model: str) -> BlockVariant:
    """
    from a given model file set up storage for textures,
    then recurse from parent models back to the given one, setting the correct textures
    """
    name = trim_filetype(model)
    parts = name.split('/')
    block_id = parts[-1]
    result = BlockVariant(block_id)
    recurse_texture_resolve(result, model)
    all_models_textures = result.fields.get("textures")

    if all_models_textures:
        for key,value in all_models_textures.items():
            if isinstance(value, dict):
                sprite = value.get("sprite")
                if sprite:
                    all_models_textures[key] = sprite

        all_parsed = False # Possible endless loop
        while not all_parsed:
            all_parsed = True
            for key,value in all_models_textures.items():
                if len(value) < 1:
                    continue
                if value[0] == '#':
                    all_parsed = False
                    for k,v in all_models_textures.items():
                        if value == '#' + k:
                            all_models_textures[key] = v
                else:
                    result.textures.append(value)

        # for key,value in all_models_textures.items():
        #     print(f"{key}   {value}")
        # exit()

    elements = result.fields.get("elements")
    if elements:
        for e in elements:
            faces = e.get("faces")
            if faces:
                i = 0
                for v in faces.values():
                    texture_placeholder = v.get("texture")
                    texture = result.textures[0]
                    for identifier,file in all_models_textures.items():
                        if texture_placeholder == '#' + identifier:
                            texture = file
                            break
                    image = open_texture(prepend_texture_path(texture))
                    pix = image.tolist()
                    uv = v.get("uv")
                    x1,y1,x2,y2 = 0,0,15,15
                    if uv:
                        x1 = int(uv[0])
                        x2 = int(uv[2])
                        y1 = int(uv[1])
                        y2 = int(uv[3])
                    used_texture = image[y1:y2,x1:x2,:]
                    save_texture(used_texture, f"{var.SCRIPT_DIR}/info/{block_id}_{i}_used.png")
                    i += 1
                    x = x1
                    while x < x2:
                        y = y1
                        while y < y2:
                            if pix[y][x][3] > 0:
                                result.pixels.append(pix[y][x])
                            y += 1
                        x += 1
    return result

def block_models() -> list[Block]:
    """
    iterate through model files extracted from blockStates
    create a Block instance for each and set its textures
    """
    block_files = list_block_models()
    blocks = []
    
    for k, v in tqdm(block_files.items(), total=len(block_files), desc="model extraction"):
        b = Block(k.removesuffix(".json"))
        for model_file in v:
            model = texture_block_from_model(model_file)
            model.block_id = b.id
            b.variants.append(model)
        blocks.append(b)

    file = open(f"{var.SCRIPT_DIR}/info/all_models_with_unique_texture_lists.txt", "w+", encoding="utf-8")
    for b in blocks:
        file.write(f"{b.id}\n")
        if len(b.variants) > 0:
            for model in b.variants:
                file.write(f"\t{model.model_id}\n")
                file.write(f"\t\t{model.textures}\n")
    file.close()
    return blocks

def prune_duplicates(blocks: list[Block]):
    for b in blocks:
        stay: list[BlockVariant] = []
        for m in b.variants:
            is_duplicate = False
            for comp in b.variants:
                if (comp.model_id == m.model_id):
                    continue
                if len(m.pixels) == len(comp.pixels):
                    mset = set(tuple(pixel) for pixel in m.pixels)
                    cset = set(tuple(pixel) for pixel in comp.pixels)
                    if (mset == cset):
                        is_duplicate = True
            if not is_duplicate:
                stay.append(m)
                
        b.variants = stay

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

def manage_props(blocks: list[Block]):
    file = open(f"{var.SCRIPT_DIR}/info/summon_suffixes_two.txt", "w+", encoding="utf-8")
    cmds = open(f"{var.SCRIPT_DIR}/info/summons.txt", "w+", encoding="utf-8")

    all_suff = []

    for b in blocks:
        for m in b.variants:
            m.groups.append("all")
            if m.block_id == m.model_id:
                continue
            suffixes = m.model_id.removeprefix(m.block_id)
            parts = re.split(r"(?=_)", suffixes)
            not_found = []
            for i in range(len(parts)):
                p = parts[i]
                p2 = None
                if i + 1 < len(parts):
                    p2 = parts[i + 1]
                p3 = None
                if i + 2 < len(parts):
                    p3 = parts[i + 2]
                pm = None
                if i - 1 >= 0:
                    pm = parts[i - 1]
                if p.startswith("_stage"): #age
                    value = p.removeprefix("_stage")
                    if "torchflower" in m.block_id:
                        m.properties.append(f'age:"{value}"')
                    elif m.block_id.startswith("cocoa"):
                        m.properties.append(f'age:"{value}"')
                    elif m.block_id.startswith("nether_wart"):
                        m.properties.append(f'age:"{value if int(value) < 2 else 3}"')
                    elif m.block_id.startswith("beet"):
                        m.properties.append(f'age:"{value}"')
                    elif m.block_id.startswith("frosted"):
                        m.properties.append(f'age:"{value}"')
                    elif m.block_id.startswith("sweet"):
                        m.properties.append(f'age:"{value}"')
                    elif m.block_id.startswith("pitcher"):
                        m.properties.append(f'age:"{value}"')
                    elif m.block_id.startswith("mangrove"):
                        m.properties.append(f'age:"{value}"')
                    elif m.block_id.startswith("chorus"):
                        m.properties.append(f'age:"{value}"')
                    elif m.block_id.startswith("wheat"):
                        m.properties.append(f'age:"{value}"')
                    elif m.block_id.startswith("pumpkin"):
                        m.properties.append(f'age:"{value}"')
                    elif m.block_id.startswith("melon"):
                        m.properties.append(f'age:"{value}"')
                    elif m.block_id.startswith("carrots"):
                        m.properties.append(f'age:"{int(value) * 2 + 1}"')
                    elif m.block_id.startswith("potatoes"):
                        m.properties.append(f'age:"{int(value) * 2 + 1}"')
                    elif m.block_id.startswith("fire"):
                        m.properties.append(f'age:"{value}"')
                    elif m.block_id.startswith("cactus"):
                        m.properties.append(f'age:"{value}"')
                    elif m.block_id.startswith("sugar"):
                        m.properties.append(f'age:"{value}"')
                    elif "vines" in m.block_id:
                        m.properties.append(f'age:"{value}"')
                    elif "kelp" in m.block_id:
                        m.properties.append(f'age:"{value}"')
                elif p == "_attatched":
                    m.properties.append('attatched:"true"')
                elif m.block_id.startswith("bell"):
                    if p == "_ceiling":
                        m.properties.append('attachment:"ceiling"')
                    if p == "_between":
                        m.properties.append('attachment:"double_wall"')
                    if p == "_floor":
                        m.properties.append('attachment:"floor"')
                    if p == "_wall":
                        m.properties.append('attachment:"single_wall"')
                elif p == "_x":
                    m.properties.append('axis:"x"')
                elif p == "_y":
                    m.properties.append('axis:"y"')
                elif p == "_z":
                    m.properties.append('axis:"z"')
                elif p == "_lit":
                    if m.block_id.startswith("cave"):
                        m.properties.append('berries:"true"')
                    m.properties.append('lit:"true"')
                elif m.block_id.startswith("cake"):
                    if p == "_slice":
                        value = p.removeprefix("_slice")
                        m.properties.append(f'bites:"{value}"')
                elif p == "_bloom":
                    m.properties.append('bloom:"true"')
                elif p == "_stable":
                    m.properties.append('bottom:"true"')
                elif p == "_side":
                    if p2 and p2 == "_tall":
                        m.properties.append('north:"tall"')
                    elif p2 and p2 == "_small":
                        m.properties.append('north:"low"')
                    elif p2 and p2 == "_north":
                        m.properties.append('north:"true"')
                    elif p2 and p2 == "_south":
                        m.properties.append('south:"true"')
                    elif p2 and p2 == "_west":
                        m.properties.append('west:"true"')
                    elif p2 and p2 == "_east":
                        m.properties.append('east:"true"')
                    elif "bars" in m.block_id or "pane" in m.block_id:
                        if p2:
                            m.properties.append('north:"true"')
                            m.properties.append('south:"true"')
                        else:
                            m.properties.append('west:"true"')
                            m.properties.append('east:"true"')
                elif p == "_pressed":
                    m.properties.append('powered:"true"')
                elif p == "_powered":
                    m.properties.append('powered:"true"')
                elif p == "_on":
                    m.properties.append('powered:"true"')
                elif p == "_open":
                    m.properties.append('open:"true"')
                elif p.startswith("_candle"):
                    if pm and pm == "_one":
                        m.properties.append('candles:"1"')
                    if pm and pm == "_two":
                        m.properties.append('candles:"2"')
                    if pm and pm == "_three":
                        m.properties.append('candles:"3"')
                    if pm and pm == "_four":
                        m.properties.append('candles:"4"')
                elif p == "_left":
                    if m.block_id.endswith("shelf"):
                        m.properties.append('side_chain:"left"')
                        m.properties.append('powered:"true"')
                    elif m.block_id.endswith("door"):
                        m.properties.append('left:"true"')
                elif p == "_right":
                    if m.block_id.endswith("shelf"):
                        m.properties.append('side_chain:"right"')
                        m.properties.append('powered:"true"')
                    elif m.block_id.endswith("door"):
                        m.properties.append('right:"true"')
                elif p == "_center":
                    m.properties.append('side_chain:"center"')
                    m.properties.append('powered:"true"')
                elif p == "_bottom":
                    m.properties.append('half:"bottom"')
                elif p == "_inner":
                    m.properties.append('shape:"inner_left"')
                elif p == "_outer":
                    m.properties.append('shape:"outer_right"')
                elif p == "_down":
                    m.properties.append('powered:"true"')
                elif p == "_offn":
                    m.properties.append('powered:"false"')
                elif p == "_north":
                    m.properties.append('north:"true"')
                elif p == "_south":
                    m.properties.append('south:"true"')
                elif p == "_west":
                    m.properties.append('west:"true"')
                elif p == "_east":
                    m.properties.append('east:"true"')
                elif p == "_leaves":
                    if pm and pm == "_large":
                        m.properties.append('leaves:"large"')
                    if pm and pm == "_small":
                        m.properties.append('leaves:"small"')
                elif p == "_honey":
                    m.properties.append('honey_level:"5"')
                elif p == "_conditional":
                    m.properties.append('conditional:"true"')
                elif p == "_slot":
                    if pm and pm == "_empty":
                        if p2 and p2 == "_top":
                            if p3 and p3 == "_left":
                                m.properties.append('slot_0_occupied:"false"')
                                m.properties.append('slot_1_occupied:"true"')
                                m.properties.append('slot_2_occupied:"true"')
                                m.properties.append('slot_3_occupied:"true"')
                                m.properties.append('slot_4_occupied:"true"')
                                m.properties.append('slot_5_occupied:"true"')
                            elif p3 and p3 == "_mid":
                                m.properties.append('slot_0_occupied:"true"')
                                m.properties.append('slot_1_occupied:"false"')
                                m.properties.append('slot_2_occupied:"true"')
                                m.properties.append('slot_3_occupied:"true"')
                                m.properties.append('slot_4_occupied:"true"')
                                m.properties.append('slot_5_occupied:"true"')
                            elif p3 and p3 == "_right":
                                m.properties.append('slot_0_occupied:"true"')
                                m.properties.append('slot_1_occupied:"true"')
                                m.properties.append('slot_2_occupied:"false"')
                                m.properties.append('slot_3_occupied:"true"')
                                m.properties.append('slot_4_occupied:"true"')
                                m.properties.append('slot_5_occupied:"true"')
                        elif p2 and p2 == "_bottom":
                            if p3 and p3 == "_left":
                                m.properties.append('slot_0_occupied:"true"')
                                m.properties.append('slot_1_occupied:"true"')
                                m.properties.append('slot_2_occupied:"true"')
                                m.properties.append('slot_3_occupied:"false"')
                                m.properties.append('slot_4_occupied:"true"')
                                m.properties.append('slot_5_occupied:"true"')
                            elif p3 and p3 == "_mid":
                                m.properties.append('slot_0_occupied:"true"')
                                m.properties.append('slot_1_occupied:"true"')
                                m.properties.append('slot_2_occupied:"true"')
                                m.properties.append('slot_3_occupied:"true"')
                                m.properties.append('slot_4_occupied:"false"')
                                m.properties.append('slot_5_occupied:"true"')
                            elif p3 and p3 == "_right":
                                m.properties.append('slot_0_occupied:"true"')
                                m.properties.append('slot_1_occupied:"true"')
                                m.properties.append('slot_2_occupied:"true"')
                                m.properties.append('slot_3_occupied:"true"')
                                m.properties.append('slot_4_occupied:"true"')
                                m.properties.append('slot_5_occupied:"false"')
                    elif pm and pm == "_occupied":
                        if p2 and p2 == "_top":
                            if p3 and p3 == "_left":
                                m.properties.append('slot_0_occupied:"true"')
                                m.properties.append('slot_1_occupied:"false"')
                                m.properties.append('slot_2_occupied:"false"')
                                m.properties.append('slot_3_occupied:"false"')
                                m.properties.append('slot_4_occupied:"false"')
                                m.properties.append('slot_5_occupied:"false"')
                            elif p3 and p3 == "_mid":
                                m.properties.append('slot_0_occupied:"false"')
                                m.properties.append('slot_1_occupied:"true"')
                                m.properties.append('slot_2_occupied:"false"')
                                m.properties.append('slot_3_occupied:"false"')
                                m.properties.append('slot_4_occupied:"false"')
                                m.properties.append('slot_5_occupied:"false"')
                            elif p3 and p3 == "_right":
                                m.properties.append('slot_0_occupied:"false"')
                                m.properties.append('slot_1_occupied:"false"')
                                m.properties.append('slot_2_occupied:"true"')
                                m.properties.append('slot_3_occupied:"false"')
                                m.properties.append('slot_4_occupied:"false"')
                                m.properties.append('slot_5_occupied:"false"')
                        elif p2 and p2 == "_bottom":
                            if p3 and p3 == "_left":
                                m.properties.append('slot_0_occupied:"false"')
                                m.properties.append('slot_1_occupied:"false"')
                                m.properties.append('slot_2_occupied:"false"')
                                m.properties.append('slot_3_occupied:"true"')
                                m.properties.append('slot_4_occupied:"false"')
                                m.properties.append('slot_5_occupied:"false"')
                            elif p3 and p3 == "_mid":
                                m.properties.append('slot_0_occupied:"false"')
                                m.properties.append('slot_1_occupied:"false"')
                                m.properties.append('slot_2_occupied:"false"')
                                m.properties.append('slot_3_occupied:"false"')
                                m.properties.append('slot_4_occupied:"true"')
                                m.properties.append('slot_5_occupied:"false"')
                            elif p3 and p3 == "_right":
                                m.properties.append('slot_0_occupied:"false"')
                                m.properties.append('slot_1_occupied:"false"')
                                m.properties.append('slot_2_occupied:"false"')
                                m.properties.append('slot_3_occupied:"false"')
                                m.properties.append('slot_4_occupied:"false"')
                                m.properties.append('slot_5_occupied:"true"')
                
                elif p == "_post" or p == "_noside" or p == "_unconnected" or  p == "_unpowered" or  p == "_empty" or  p == "_large" or  p == "_small" or  p == "_mirrored" \
                        or p == "_one" or p == "_two" or p == "_three" or p == "_four" or p == "_cap" or p == "_alt":
                    continue
                

                else:
                    not_found.append(p)
            if len(not_found) > 1:
                all_suff.append("".join(not_found) + "\t\t" + m.model_id)

    # unique = set(all_suff)
    for s in all_suff:
        file.write(f"{s}\n")
    file.close()

def manage_summons(blocks: list[Block]):
    file = open(f"{var.SCRIPT_DIR}/info/summon_suffixes.txt", "w+", encoding="utf-8")
    cmds = open(f"{var.SCRIPT_DIR}/info/summons.txt", "w+", encoding="utf-8")
    skips = ("sign", "banner", "_z", "_x", "_top_left", "_side_east", "_honey", "_one_candle_lit", 
             "_side_", "_top", "air",
             "_empty_slot_top_mid", "_wall", "_up1", "_side1", "water", "lava", "skull",
             "_00", "_01", "_02", "_03", "_04", "_05", "_06", "_07", "_08", "_09", "_10", "_11", "_12", "_13", "_14", "_15", # pure light blocks
             "_stage1", "_stage2", "_stage3", "_stage4", "_stage5", "_stage6", "_stage7", # crops
             "_hydration_1", "_hydration_2", "_hydration_3", # ghasts
             )
    for b in blocks:
        core = b.id
        for m in b.variants:
            shortest = m.block_id
            if shortest == core:
                m.summons.append(shortest)
                cmds.write(f"{shortest}\n")
                continue
            suffixes = shortest.removeprefix(core)
            is_skip = any(skip in suffixes for skip in skips)
            # file.write(f"{suffixes}\t\t{shortest}\n")
            if is_skip or core.startswith("waxed") or core.startswith("infested"):
                continue
            elif suffixes == "_y" or suffixes == "_up0" or suffixes == "_side0" or suffixes == "_ns" or suffixes == "_n":
                m.summons.append(core)
            elif "_bottom" in suffixes: # blocks that are 2 tall → doors / big flowers
                m.summons.append(core + 'half:"upper"') 
                m.summons.append(core + 'half:"lower"')
            elif suffixes == "_post": # fences, walls, panes, bars
                m.summons.append(core + 'north:"true",south:"true"')
                m.summons.append(core + 'west:"true",east:"true"')
            elif suffixes.endswith("_cap"): # bars go to this and not _post
                m.summons.append(core + 'north:"true",south:"true"')
                m.summons.append(core + 'west:"true",east:"true"')
            elif suffixes == "_open": # trap doors
                m.summons.append(core + 'half:"bottom"')
                m.summons.append(core + 'open:"true"')
            elif suffixes == "1_age0": # bamboo
                m.summons.append(core + 'leaves:"none"')
            elif suffixes == "_small_leaves": # bamboo
                m.summons.append(core + 'leaves:"small"')
            elif suffixes == "_large_leaves": # bamboo
                m.summons.append(core + 'leaves:"large"')
            elif suffixes == "_on": # rails furnaces, redstone components, lightning rods ...
                m.summons.append(core + 'on:"true",lit:"true",powered:"true"')
            elif suffixes == "_open": # barrels
                m.summons.append(core + 'open:"true"')
            elif "_occupied" in suffixes: # chiseled bookshelf
                m.summons.append(core + 'slot_0_occupied:"true",slot_1_occupied:"true",slot_2_occupied:"true",slot_3_occupied:"true",slot_4_occupied:"true",slot_5_occupied:"true"')
            elif suffixes == "_empty": # bees
                m.summons.append(core + 'honey_level:"false"')
                m.summons.append(core + 'honey_level:"true"')
            elif "_stage0" in  suffixes:
                if "cocoa" in shortest:
                    m.summons.append(core + 'age:"0"')
                    m.summons.append(core + 'age:"1"')
                    m.summons.append(core + 'age:"2"')
                if "nether_wart" in shortest:
                    m.summons.append(core + 'age:"0"')
                    m.summons.append(core + 'age:"1"')
                    m.summons.append(core + 'age:"3"') # really weird
                elif "berry" in shortest or "beetroots" in shortest:
                    m.summons.append(core + 'age:"0"')
                    m.summons.append(core + 'age:"1"')
                    m.summons.append(core + 'age:"2"')
                    m.summons.append(core + 'age:"3"')
                elif "carrots" in shortest or "potatoes" in shortest:
                    m.summons.append(core + 'age:"1"')
                    m.summons.append(core + 'age:"3"')
                    m.summons.append(core + 'age:"5"')
                    m.summons.append(core + 'age:"7"')
                elif "wheat" in shortest:
                    m.summons.append(core + 'age:"0"')
                    m.summons.append(core + 'age:"1"')
                    m.summons.append(core + 'age:"2"')
                    m.summons.append(core + 'age:"3"')
                    m.summons.append(core + 'age:"4"')
                    m.summons.append(core + 'age:"5"')
                    m.summons.append(core + 'age:"6"')
                    m.summons.append(core + 'age:"7"')
            elif suffixes == "bed":
                m.summons.append(core + 'part:"foot"')
            elif suffixes == "_one_candle":
                m.summons.append(core + 'candles:"1"')
                m.summons.append(core + 'candles:"2"')
                m.summons.append(core + 'candles:"3"')
                m.summons.append(core + 'candles:"4"')
                m.summons.append(core + 'candles:"1",lit:"true"')
                m.summons.append(core + 'candles:"2",lit:"true"')
                m.summons.append(core + 'candles:"3",lit:"true"')
                m.summons.append(core + 'candles:"4",lit:"true"')
            elif suffixes == "_hydration_0":
                m.summons.append(core + 'hydration:"0"')
                m.summons.append(core + 'hydration:"1"')
                m.summons.append(core + 'hydration:"2"')
                m.summons.append(core + 'hydration:"3"')
            elif suffixes == "mushroom_block_inside":
                if core == "brown_mushroom_block":
                    m.summons.append(core + 'north:"false",south:"false",east:"false",west:"false",up:"false",down:"false"')
            elif suffixes == "_active":
                if "sculk" in core:
                    m.summons.append(core + 'sculk_sensor_phase:"active"')
                    m.summons.append(core + 'sculk_sensor_phase:"inactive"')
                elif "vault" in core:
                    m.summons.append(core + 'vault_state:"active"')
                else:
                    m.summons.append(core + 'trial_spawner_state:"active"')
            elif core.endswith("slab"):
                m.summons.append(core + 'half:"top"')
                m.summons.append(core + 'half:"bottom"')
                m.summons.append(core + 'type:"double"')
            elif suffixes == "_conditional":
                m.summons.append(core + 'conditional:"true"')
            elif suffixes == "_vertical":
                m.summons.append(core + 'facing:"up"')
            elif suffixes == "_lit_powered":
                m.summons.append(core + 'lit:"true",powered:"true"')
            elif suffixes == "_powered":
                m.summons.append(core + 'powered:"true"')
            elif suffixes == "_lit":
                if core.startswith("cave_vines"):
                    m.summons.append(core + 'age:"24",berries:"true"')
                else:
                    m.summons.append(core + 'lit:"true"')
            elif suffixes == "_side":
                m.summons.append(core)
            elif suffixes == "_snow" or suffixes == "grass_block_snow":
                m.summons.append(core + 'snowy:"true"')
            elif suffixes == "lightning_rod_on": # weatthered variants fall back to original
                m.summons.append(core + 'powered:"true"')
            elif suffixes == "_0":
                if "frosted" in core:
                    m.summons.append(core + 'age:"0"')
                    m.summons.append(core + 'age:"1"')
                    m.summons.append(core + 'age:"2"')
                    m.summons.append(core + 'age:"3"')
                elif "respawn" in core:
                    m.summons.append(core + 'charges:"0"')
                    m.summons.append(core + 'charges:"1"')
                    m.summons.append(core + 'charges:"2"')
                    m.summons.append(core + 'charges:"3"')
                    m.summons.append(core + 'charges:"4"')
                elif "suspicious" in core:
                    m.summons.append(core + 'dusted:"0"')
                    m.summons.append(core + 'dusted:"1"')
                    m.summons.append(core + 'dusted:"2"')
                    m.summons.append(core + 'dusted:"3"')
                else:
                    m.summons.append(core + 'segment_amount:"1"')
                    m.summons.append(core + 'segment_amount:"2"')
                    m.summons.append(core + 'segment_amount:"3"')
                    m.summons.append(core + 'segment_amount:"4"')
            elif suffixes == "_1" or suffixes == "_2" or suffixes == "_3" or suffixes == "_4" or suffixes == "_base" or suffixes == "piston_base" or suffixes == "_full":
                continue
            elif suffixes == "_off":
                m.summons.append(core + 'powered:"false"')
            elif suffixes == "_1tick":
                m.summons.append(core + 'delay:"0"')
                m.summons.append(core + 'delay:"1"')
                m.summons.append(core + 'delay:"2"')
                m.summons.append(core + 'delay:"3"')
            elif suffixes == "_1tick_on":
                m.summons.append(core + 'delay:"0",powered:"true"')
                m.summons.append(core + 'delay:"1",powered:"true"')
                m.summons.append(core + 'delay:"2",powered:"true"')
                m.summons.append(core + 'delay:"3",powered:"true"')
            elif suffixes == "_not_cracked":
                m.summons.append(core + 'hatch:"0"')
            elif suffixes == "_slightly_cracked":
                m.summons.append(core + 'hatch:"1"')
            elif suffixes == "_very_cracked":
                m.summons.append(core + 'hatch:"2"')
            elif suffixes == "_height2":
                m.summons.append(core + 'layers:"1"')
                m.summons.append(core + 'layers:"2"')
                m.summons.append(core + 'layers:"3"')
                m.summons.append(core + 'layers:"4"')
                m.summons.append(core + 'layers:"5"')
                m.summons.append(core + 'layers:"6"')
                m.summons.append(core + 'layers:"7"')
                m.summons.append(core + 'layers:"8"')

            else:
                file.write(f"{suffixes}\t\t{shortest}\n")
    file.close()

def filter_blocks(blocks: list[Block]):
    """
    assign groups for each block
    """
    colors = ("black", "blue", "brown", "cyan", "gray", "green", "light_blue", "light_gray", "lime", "magenta", "orange", "pink", "purple", "red", "white", "yellow")
    woods = ("acacia", "birch", "cherry", "crimson", "dark_oak", "jungle", "mangrove", "pale", "oak", "warped", "spruce")
    rocks = ("stone", "diorite", "granite", "andesite", "basalt")
    for b in blocks:
        is_color = any(color in b.id for color in colors)
        is_wood = any(wood in b.id for wood in woods)
        is_rock = any(rock in b.id for rock in rocks)

        for m in b.variants:
            if is_color:
                m.groups.append("color")
            if is_wood:
                m.groups.append("wood")
            if is_rock:
                m.groups.append("rock")

def store_blocks(blocks: list[Block]):
    for b in tqdm(blocks, total=len(blocks), desc="storing_models"):
        for m in b.variants:
            m.fields["block_id"] = m.block_id
            m.fields["model_id"] = m.model_id
            m.fields["pixels"] = []
            m.fields["summons"] = []
            m.fields["properties"] = []
            for p in m.pixels:
                m.fields["pixels"].append(p)
            for s in m.summons:
                m.fields["summons"].append(s)
            for p in m.properties:
                m.fields["properties"].append(p)
            file = open(f"{var.SCRIPT_DIR}/models/{m.model_id}", "w+", encoding="utf-8")
            json.dump(m.fields, file)
            file.close()

def load_blocks() -> list[Block]:
    collection: dict[str, Block] = {}
    files = list(Path(f"{var.SCRIPT_DIR}/models/").iterdir())

    for file_path in tqdm(files, desc="load models", unit="file"):
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        model = BlockVariant(data["model_id"])
        model.block_id = data["block_id"]
        model.pixels = data["pixels"]
        model.properties = data["properties"]
        model.summons = data["summons"]

        model.textures = data["textures"]

        if model.block_id not in collection:
            collection[model.block_id] = Block(model.block_id)
            
        collection[model.block_id].variants.append(model)

    return list(collection.values())


if __name__ == "__main__":

    m = texture_block_from_model("/mnt/c/Users/Clemens/Documents/ColorTheory/Minecraft-default-assets/assets/minecraft/models/block/cake.json")
    m2 = texture_block_from_model("/mnt/c/Users/Clemens/Documents/ColorTheory/Minecraft-default-assets/assets/minecraft/models/block/cake_slice1.json")

    b = Block("bamboo_block")
    m.block_id = b.id
    m2.block_id = b.id
    b.variants.append(m)
    b.variants.append(m2)
    bs = []
    bs.append(b)
    prune_duplicates(bs)
    manage_props(bs)
    print(m.properties)
    print(m2.properties)

    file = open(f"{var.SCRIPT_DIR}/info/combined.json", "w+", encoding="utf-8")
    json.dump(m.pixels, file)
    file.close()
    file = open(f"{var.SCRIPT_DIR}/info/combined2.json", "w+", encoding="utf-8")
    json.dump(m2.pixels, file)
    file.close()

    print(len(m.pixels))
    print(len(m2.pixels))

    # blocks = block_models()

    # manage_summons(blocks)
    
    # filter_blocks(blocks)
    
    pass

