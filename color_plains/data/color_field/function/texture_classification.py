import variables as var
import mc_writer
from block_class import Block
from block_class import BlockVariant
import json
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
    suffixes = defaultdict(list)
    def get_base(name):
        name = trim_filetype(name)
        parts = name.split("_")
        while len(parts) > 0:
            suffixes[parts[-1]] = parts[0]
            parts.pop()
        return (name)

    files = [f.name for f in Path(var.model_folder).iterdir() if f.is_file()]

    blocks = defaultdict(list)

    for f in files:
        base = get_base(f)

        blocks[base].append(f + ".png")
    return dict(blocks)

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

    file = open(f"{var.SCRIPT_DIR}/info/all_models.txt", "w+")
    for k,v in key.items():
        for m in v:
            file.write(f"{m}\n")
    file.close()

    return (key)

def recurse_texture_resolve(block: BlockVariant, model: str):
    """
    opens the current model and if it has a parent model that isnt itself → recurse
    set the fields that the model defines
    """
    try:
        file = open(model)
    except Exception:
        print("opening issue")
        print(model)
        return
    info = json.load(file)
    file.close()
    name = trim_filetype(model)
    parent = info.get("parent")
    if parent:
        parent = prepend_model_path(parent)
        if parent != name:
            recurse_texture_resolve(block, f"{parent}.json")
    textures = info.get("textures")
    if textures:
        for k, v in textures.items():
            if isinstance(v, dict): # glass models are funky
                if "sprite" in v:
                    v = v["sprite"]
            for bk, bv in block.textures.items():
                if k == bk and len(v) > 1 and v[0] == '#':
                    block.textures[bk] = v
                elif (bv == "") or (bv == '#' + k):
                    block.textures[bk] = v
    pass

def texture_block_from_model(model: str) -> BlockVariant:
    """
    from a given model file set up storage for textures,
    then recurse from parent models back to the given one, setting the correct textures
    """
    name = trim_filetype(model)
    result = BlockVariant(name)
    recurse_texture_resolve(result, model)
    for k, v in result.textures.items():
        result.textures[k] = v
    return result

def block_models() -> list[Block]:
    """
    iterate through model files extracted from blockStates
    create a Block instance for each and set its textures
    """
    block_files = list_block_models()
    blocks = []
    
    for k,v in block_files.items():
        b = Block(k)
        for model_file in v:
            model = texture_block_from_model(model_file)
            if not (model.textures["north"] or model.textures["south"] \
                or model.textures["west"] or model.textures["east"] \
                or model.textures["up"] or model.textures["down"] \
                or model.textures["particle"]):
                print(f"failed resolving texture for\n{model.identifier}")
                continue
            duplicate_exists = any(model.textures == existing.textures for existing in b.variants)
            if not duplicate_exists:
                b.variants.append(model)
        blocks.append(b)

    file = open(f"{var.SCRIPT_DIR}/info/all_models_with_unique_texture_lists.txt", "w+")
    for b in blocks:
        file.write(f"{len(b.variants)}\t{b.id}\n")
        if len(b.variants) > 0:
            for model in b.variants:
                file.write(f"\t\t{model.textures}\n")
    file.close()
    return blocks

def filter_blocks(blocks: list[Block]):
    """
    some models are defined through block state and model files, tho it seems wrong
    like how banners get the textures of oak_planks
    same with beds
    all heads get assigned the texture of soul_sand
    """
    pass


if __name__ == "__main__":
    blocks = block_models()

    pass

