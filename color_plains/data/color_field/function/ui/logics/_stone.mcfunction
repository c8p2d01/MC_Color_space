execute if score @s cf_block_stone matches 1 run scoreboard players set @s cf_block_stone 2
execute unless score @s cf_block_stone matches 1..2 run scoreboard players set @s cf_block_stone 1
execute if score @s cf_block_stone matches 2 run scoreboard players set @s cf_block_stone 0
execute as @s run kill @e[type=text_display,tag=ui_block_stone]
execute as @s run function color_field:ui/elements/_stone
function color_field:render/set/set_blocks