import variables as var

def char_replace(s, c='_', n='\\n'):
    parts = s.split(c)
    joined = n.join(parts)
    return (joined)

def create_ui_element(group, pos_layer, pos_angle):
    return (
        f"execute if score @s cf_block_{group} matches 1 as @e[type=interaction,tag=layer_{pos_layer},tag=yawstep_{pos_angle}] at @s run "\
        f"summon text_display ^ ^ ^ {{"\
        f"Tags:[\"color_field\",\"color_field_ui\",\"ui_block_{group}\"],"\
        f"text:{{\"text\":\"{char_replace(group)}\",\"color\":\"green\"}},"\
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
            f"text:{{\"text\":\"{char_replace(group)}\",\"color\":\"dark_gray\"}},"\
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



def create_summon_string_text(x, y, z, r, g, b, d, type):
    return (\
        f"execute as @e[tag=color_field_anchor,limit=1] at @s run summon text_display "\
        f"~{(x + var.HALF):.4f} ~{(y + var.HALF):.4f} ~{(z + var.HALF):.4f} {{"\
        f"Tags:[\"color_field\",\"color_field_node\",\"render_{type}\",\"density_{d}\"],"\
        f"text:{{\"text\":\"⬤\",\"color\":\"#{int(r % 256):02x}{int(g % 256):02x}{int(b % 256):02x}\"}},"\
        f"background:0,"\
        f"brightness:{{block:15,sky:15}},"\
        f"billboard:\"center\","\
        f"transformation:{{"\
        f"translation:[0f,0f,0f],"\
        f"left_rotation:[0f,0f,0f,1f],"\
        f"right_rotation:[0f,0f,0f,1f],"\
        f"scale:[{var.CUBE_SIZE / 4}f,{var.CUBE_SIZE / 4}f,{var.CUBE_SIZE / 4}f]"\
        f"}}"\
        f"}}\n"\
    )

def create_summon_string(x, y, z, block, group, scale_divisor=32):
    return (\
        f"execute as @e[tag=color_field_anchor,limit=1] at @s run summon block_display "\
        f"~{(x + var.HALF):.4f} ~{(y + var.HALF):.4f} ~{(z + var.HALF):.4f} {{"\
        f"Tags:[\"color_field\",\"color_field_block\",\"render_{group}\"],"\
        f"block_state:{{Name:\"{block}\"}},"\
        f"brightness:{{block:15,sky:15}},"\
        f"transformation:{{"\
        f"translation:[0f,0f,0f],"\
        f"left_rotation:[0f,0f,0f,1f],"\
        f"right_rotation:[0f,0f,0f,1f],"\
        f"scale:[{var.CUBE_SIZE / scale_divisor}f,{var.CUBE_SIZE / scale_divisor}f,{var.CUBE_SIZE / scale_divisor}f]"\
        f"}}"\
        f"}}\n"\
    )

def create_ui_logic(group):
    return (
        f"execute if score @s cf_block_{group} matches 1 run scoreboard players set @s cf_block_{group} 2\n"\
        f"execute unless score @s cf_block_{group} matches 1..2 run scoreboard players set @s cf_block_{group} 1\n"\
        f"execute if score @s cf_block_{group} matches 2 run scoreboard players set @s cf_block_{group} 0\n"\
        f"execute as @s run kill @e[type=text_display,tag=ui_block_{group}]\n"\
        f"execute as @s run function color_field:ui/elements/_{group}\n"\
        f"function color_field:render/set/set_blocks"\
    )

def create_render_logic(group):
    return (\
        f"# {group}\n"\
        f"execute \\\n"\
        f"if score @s cf_coltype matches 8 \\\n"\
        f"if score @s cf_block_{group} matches 1 \\\n"\
        f"run function color_field:render/blocks/rgb/{group}\n"\
        f"execute \\\n"\
        f"if score @s cf_coltype matches 9 \\\n"\
        f"if score @s cf_block_{group} matches 1 \\\n"\
        f"run function color_field:render/blocks/hsl/{group}\n"\
        f"execute \\\n"\
        f"if score @s cf_coltype matches 10 \\\n"\
        f"if score @s cf_block_{group} matches 1 \\\n"\
        f"run function color_field:render/blocks/lab/{group}\n"\
        f"execute \\\n"\
        f"if score @s cf_coltype matches 11 \\\n"\
        f"if score @s cf_block_{group} matches 1 \\\n"\
        f"run function color_field:render/blocks/oklab/{group}\n"\
        f"execute \\\n"\
        f"if score @s cf_coltype matches 12 \\\n"\
        f"if score @s cf_block_{group} matches 1 \\\n"\
        f"run function color_field:render/blocks/oklch/{group}\n\n"\
    )

if __name__ == "__main__":
    pass
