execute if score @s cf_block_concrete_powder matches 1 run scoreboard players set @s cf_block_concrete_powder 2
execute unless score @s cf_block_concrete_powder matches 1..2 run scoreboard players set @s cf_block_concrete_powder 1
execute if score @s cf_block_concrete_powder matches 2 run scoreboard players set @s cf_block_concrete_powder 0
# kill @e[type=text_display,tag="ui_block_concrete_powder"]
# function color_field:ui/elements/_concrete_powder
function color_field:render/blocks/set