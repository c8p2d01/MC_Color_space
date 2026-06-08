
# ----------------------------------------
# CLEAR OLD SPACE
# ----------------------------------------

kill @e[type=marker,tag=color_field_anchor]
function color_field:render/clear

# ----------------------------------------
# CREATE NEW ANCHOR
# ----------------------------------------

execute at @s anchored eyes run summon marker ^ ^ ^10 \
{Tags:["color_field_anchor"],Invisible:1b}

execute as @e[type=marker,tag=color_field_anchor,limit=1] at @s run tp @s ~ ~ ~ 0 0

kill @e[type=block_display,tag=color_field_cube]
kill @e[type=text_display,tag=color_field_anchor_visual]
execute if entity @s[tag=cf_anchor_on] run function color_field:render/functions/render_anchor
execute if entity @s[tag=cf_cube_on] run function color_field:render/functions/render_box

clear @p carrot_on_a_stick[custom_data={color_field:{render_wand:true}}]
scoreboard players set @s click_wand 0

function color_field:render/render