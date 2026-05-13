# ----------------------------------------
# CLEAR OLD SPACE
# ----------------------------------------

kill @e[type=marker,tag=color_field_anchor]
kill @e[type=text_display,tag=color_field_anchor_visual]
kill @e[type=text_display,tag=color_field_cube]
function color_field:render/clear
execute run tag @s add cf_cube_off

# ----------------------------------------
# CREATE NEW ANCHOR
# ----------------------------------------

execute at @s run summon marker ~ ~ ~ \
{Tags:["color_field_anchor"],Invisible:1b}

# anchor visual
execute at @s run summon text_display ~ ~ ~ \
{\
    Tags:["color_field_anchor_visual"],\
    billboard:"center",\
    text:{"text":"⬤","color":"#0d0d0d"},\
    background:0,\
    transformation:{\
        left_rotation:[0f,0f,0f,1f],\
        right_rotation:[0f,0f,0f,1f],\
        translation:[0f,0f,0f],\
        scale:[1f,1f,1f]\
    }\
}

# ----------------------------------------
# NORMALIZE ROTATION FRAME
# ----------------------------------------

function color_field:render/space/update_rotation

# ----------------------------------------
# STORE POSITION (for future field systems)
# ----------------------------------------

data modify storage color_field:ui anchorPos \
set from entity @e[type=marker,tag=color_field_anchor,limit=1] Pos

# feedback
tellraw @s {"text":"Color Field anchor initialized","color":"green"}

function color_field:ui/set_location