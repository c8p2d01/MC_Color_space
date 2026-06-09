import MC_Color_space.color_plains.data.color_field.function.variables as var
import MC_Color_space.color_plains.data.color_field.function.color_conversion as colmath
import MC_Color_space.color_plains.data.color_field.function.mc_writer as mc_writer
from MC_Color_space.color_plains.data.color_field.function.datapack_logic import generate_logic
import MC_Color_space.color_plains.data.color_field.function.texture_analysis as tsys
import MC_Color_space.color_plains.data.color_field.function.texture_classification as tclass
import numpy as np
import pandas as pd
import ast
from PIL import Image
from pathlib import Path
from collections import defaultdict
from MC_Color_space.color_plains.data.color_field.function.block_class import Block
from MC_Color_space.color_plains.data.color_field.function.block_class import BlockVariant

try:
    from pyclustering.cluster.clique import clique
    CLIQUE_AVAILABLE = True
except ImportError:
    CLIQUE_AVAILABLE = False

def test_summon(blocks: list[Block]):
    file = open(str(var.SCRIPT_DIR) + "/test_summon_all.mcfunction", "w+")
    debug = open(str(var.SCRIPT_DIR) + "/info/summons", "w+")
    x = 0
    z = 0
    for b in blocks:
        file.write(\
            mc_writer.create_summon_string_block(x, 0, z, b.id, "all_blocks", scale_divisor=var.CUBE_SIZE)
            )
        debug.write(f"{b.id.removesuffix('.json')}\n")
        x += 2
        if x >= 80:
            x = 0
            z  += 2
            debug.write("\n")
    file.close()
    debug.close()

def test_variant_summon(blocks: list[Block]):
    file = open(str(var.SCRIPT_DIR) + "/test_summon_variants.mcfunction", "w+")
    x = 0
    z = 0
    for b in blocks:
        for m in b.variants:
            for s in m.summons:
                file.write(\
                    mc_writer.create_summon_string_block(x, 0, z, b.id, "all_blocks", scale_divisor=var.CUBE_SIZE, properties=s.removeprefix(b.id))
                    )
                x += 2
                if x >= 80:
                    x = 0
                    z  += 2
    file.close()

def test_group_summon(blocks: list[Block], groups: list[str]):
    file = open(str(var.SCRIPT_DIR) + "/test_group_summon.mcfunction", "w+")
    debug = open(str(var.SCRIPT_DIR) + "/info/test_summons", "w+")
    z = {}
    for g in groups:
        z[g] = 0
    for b in blocks:
        
        debug.write(f"{b.id.removesuffix('.json')}\n")
        x += 2
        if x >= 80:
            x = 0
            z  += 2
            debug.write("\n")
    file.close()
    debug.close()



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
    mc_writer.create_render_box()

    blocks = tclass.block_models()
    # # filter_blocks(blocks)
    tclass.manage_summons(blocks)

    test_variant_summon(blocks)

    test_summon(blocks)

    # data = frame_blocks(blocks)

    # generate_logic(data)
    
    # try:
    #     generate_summons(data)
    # except Exception as e:
    #     print(f"Error: {e}\n")

    pass
