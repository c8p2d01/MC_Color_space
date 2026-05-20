execute if score @s cf_block_sculk matches 1 run scoreboard players set @s cf_block_sculk 2
execute unless score @s cf_block_sculk matches 1..2 run scoreboard players set @s cf_block_sculk 1
execute if score @s cf_block_sculk matches 2 run scoreboard players set @s cf_block_sculk 0
# kill @e[type=text_display,tag="ui_block_sculk"]
# function color_field:ui/elements/_sculk
function color_field:render/blocks/set