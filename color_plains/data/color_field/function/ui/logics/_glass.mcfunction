execute if score @s cf_block_glass matches 1 run scoreboard players set @s cf_block_glass 2
execute unless score @s cf_block_glass matches 1..2 run scoreboard players set @s cf_block_glass 1
execute if score @s cf_block_glass matches 2 run scoreboard players set @s cf_block_glass 0
# kill @e[type=text_display,tag="ui_block_glass"]
# function color_field:ui/elements/_glass
function color_field:render/blocks/set