# ----------------------------------------
# MARK CURRENT STATE
# ----------------------------------------

execute if score @s cf_cube matches 1 run \
tag @s add cf_cube_on

execute unless score @s cf_cube matches 1 run \
tag @s add cf_cube_off

# ----------------------------------------
# TURN OFF RENDER
# ----------------------------------------

execute if entity @s[tag=cf_cube_on] run \
kill @e[type=text_display,tag=color_field_cube]

execute if entity @s[tag=cf_cube_on] run \
kill @e[type=text_display,tag=color_field_anchor_visual]

execute if entity @s[tag=cf_cube_on] run \
scoreboard players set @s cf_cube 0

# ----------------------------------------
# TURN ON RENDER
# ----------------------------------------

# rebuild anchor visual
execute if entity @s[tag=cf_cube_off] at @e[type=marker,tag=color_field_anchor,limit=1] run \
summon text_display ~ ~ ~ \
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

# rebuild cube
execute if entity @s[tag=cf_cube_off] run \
function color_field:render/space/cube

# update scoreboard
execute if entity @s[tag=cf_cube_off] run \
scoreboard players set @s cf_cube 1

# ----------------------------------------
# CLEANUP
# ----------------------------------------

tag @s remove cf_cube_on
tag @s remove cf_cube_off
