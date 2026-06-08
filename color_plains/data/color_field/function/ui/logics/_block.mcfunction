execute if score @s cf_block_block matches 1 run scoreboard players set @s cf_block_block 2
execute unless score @s cf_block_block matches 1..2 run scoreboard players set @s cf_block_block 1
execute if score @s cf_block_block matches 2 run scoreboard players set @s cf_block_block 0
execute as @s run kill @e[type=text_display,tag=ui_block_block]
execute as @s run function color_field:ui/elements/_block
function color_field:render/set/set_blocks