execute if score @s cf_block_ice matches 1 run scoreboard players set @s cf_block_ice 2
execute unless score @s cf_block_ice matches 1..2 run scoreboard players set @s cf_block_ice 1
execute if score @s cf_block_ice matches 2 run scoreboard players set @s cf_block_ice 0
execute as @s run kill @e[type=text_display,tag=ui_block_ice]
execute as @s run function color_field:ui/elements/_ice
function color_field:render/set/set_blocks