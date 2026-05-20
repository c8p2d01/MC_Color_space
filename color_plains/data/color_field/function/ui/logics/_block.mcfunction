execute if score @s cf_block_block matches 1 run scoreboard players set @s cf_block_block 2
execute unless score @s cf_block_block matches 1..2 run scoreboard players set @s cf_block_block 1
execute if score @s cf_block_block matches 2 run scoreboard players set @s cf_block_block 0
# kill @e[type=text_display,tag="ui_block_block"]
# function color_field:ui/elements/_block
function color_field:render/blocks/set