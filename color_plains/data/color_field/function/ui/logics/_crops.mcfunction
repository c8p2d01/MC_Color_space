execute if score @s cf_block_crops matches 1 run scoreboard players set @s cf_block_crops 2
execute unless score @s cf_block_crops matches 1..2 run scoreboard players set @s cf_block_crops 1
execute if score @s cf_block_crops matches 2 run scoreboard players set @s cf_block_crops 0
# kill @e[type=text_display,tag="ui_block_crops"]
# function color_field:ui/elements/_crops
function color_field:render/blocks/set