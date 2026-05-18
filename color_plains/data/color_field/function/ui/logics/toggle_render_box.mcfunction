# toggle on
execute if entity @s[tag=!cf_cube_on] run function color_field:render/functions/render_box
execute if entity @s[tag=!cf_cube_on] run tag @s add cf_cube_on_temp

# toggle off
execute if entity @s[tag=cf_cube_on] run kill @e[type=block_display,tag=color_field_cube]
execute if entity @s[tag=cf_cube_on] run tag @s remove cf_cube_on

# clean tags
execute if entity @s[tag=cf_cube_on_temp] run tag @s add cf_cube_on
tag @s remove cf_cube_on_temp

execute if score @s cf_feedback matches 1 run tellraw @a {"text":"toggled box visual","color":"aqua"}