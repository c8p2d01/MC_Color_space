# toggle on
execute if entity @s[tag=!cf_anchor_on] run function color_field:render/functions/render_anchor
execute if entity @s[tag=!cf_anchor_on] run tag @s add cf_anchor_on_temp

# toggle off
execute if entity @s[tag=cf_anchor_on] run kill @e[type=text_display,tag=color_field_anchor_visual]
execute if entity @s[tag=cf_anchor_on] run tag @s remove cf_anchor_on

# clean tags
execute if entity @s[tag=cf_anchor_on_temp] run tag @s add cf_anchor_on
tag @s remove cf_anchor_on_temp

execute if score @s cf_feedback matches 1 run tellraw @a {"text":"toggled anchor visual","color":"aqua"}