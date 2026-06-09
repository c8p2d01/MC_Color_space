import variables as var
import mc_writer
import shutil

def open_from_template(template: str):
    template_file = template + "_template"
    target_file = template + ".mcfunction"
    shutil.copy2(template_file, target_file)
    result = open(target_file, "a+")
    return result


def add_on_load(load_file, group):
    load_file.write(f"scoreboard objectives add cf_block_{group} dummy\n")
    load_file.write(f"execute as @p run scoreboard players set @s cf_block_{group} 0\n")

def add_click(click_file, g):
    click_file.write(f"execute if entity @s[tag=toggle_{g}] if data entity @s interaction.player on target run function color_field:ui/logics/_{g}\n")

def add_build(build_file, g):
    build_file.write(f"function color_field:ui/elements/_{g}\n")

def add_render(render_file, g):
    render_file.write(mc_writer.create_render_logic(g))

def render_append_interaction(render_file):
    """this element needs to be summoned last upon rendering"""

    render_file.write(\
        f"execute as @e[tag=color_field_anchor,limit=1] at @s run summon interaction ~ ~ ~ "\
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

def tick_append_interaction(tick_file):
    tick_file.write(\
        f"execute as @e[tag=block_shifter] at @s if entity @p[distance=..5,limit=1] run "\
        f"tp @s ~{var.CUBE_SIZE / 64} ~ ~{var.CUBE_SIZE / 64}"
    )

def click_append_interaction(click_file):
    click_file.write("\ndata remove entity @s interaction\n")

def generate_logic(groups):
    layer = 4
    angle = 330
    load = open_from_template(f"{var.SCRIPT_DIR}/load")
    tick = open_from_template(f"{var.SCRIPT_DIR}/tick")
    build = open_from_template(f"{var.SCRIPT_DIR}/ui/build_ui")
    click = open_from_template(f"{var.SCRIPT_DIR}/ui/click")
    render = open_from_template(f"{var.SCRIPT_DIR}/render/render")
    for g in groups:
        add_on_load(load, g)
        add_click(click, g)
        add_build(build, g)
        add_render(render, g)
        mc_writer.create_ui_element(f"{var.SCRIPT_DIR}/ui/elements/_{g}.mcfunction", g, layer, angle)
        mc_writer.create_ui_logic(f"{var.SCRIPT_DIR}/ui/logics/_{g}.mcfunction", g)
        layer -= 1
        if (layer < 1):
            layer = 4
            angle -= 15
    render_append_interaction(render)
    tick_append_interaction(tick)
    click_append_interaction(click)

if __name__ == "__main__":
    pass
