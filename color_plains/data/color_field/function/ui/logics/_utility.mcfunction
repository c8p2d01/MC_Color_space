execute if score @s cf_block_utility matches 1 run scoreboard players set @s cf_block_utility 2
execute unless score @s cf_block_utility matches 1..2 run scoreboard players set @s cf_block_utility 1
execute if score @s cf_block_utility matches 2 run scoreboard players set @s cf_block_utility 0
# kill @e[type=text_display,tag="ui_block_utility"]
# function color_field:ui/elements/_utility
function color_field:render/blocks/set