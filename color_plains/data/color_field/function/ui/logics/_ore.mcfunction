execute if score @s cf_block_ore matches 1 run scoreboard players set @s cf_block_ore 2
execute unless score @s cf_block_ore matches 1..2 run scoreboard players set @s cf_block_ore 1
execute if score @s cf_block_ore matches 2 run scoreboard players set @s cf_block_ore 0
# kill @e[type=text_display,tag="ui_block_ore"]
# function color_field:ui/elements/_ore
function color_field:render/blocks/set