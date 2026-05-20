execute if score @s cf_block_concrete matches 1 run scoreboard players set @s cf_block_concrete 2
execute unless score @s cf_block_concrete matches 1..2 run scoreboard players set @s cf_block_concrete 1
execute if score @s cf_block_concrete matches 2 run scoreboard players set @s cf_block_concrete 0
# kill @e[type=text_display,tag="ui_block_concrete"]
# function color_field:ui/elements/_concrete
function color_field:render/blocks/set