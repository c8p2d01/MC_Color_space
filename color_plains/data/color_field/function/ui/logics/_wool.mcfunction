execute if score @s cf_block_wool matches 1 run scoreboard players set @s cf_block_wool 2
execute unless score @s cf_block_wool matches 1..2 run scoreboard players set @s cf_block_wool 1
execute if score @s cf_block_wool matches 2 run scoreboard players set @s cf_block_wool 0
execute as @s run kill @e[type=text_display,tag=ui_block_wool]
execute as @s run function color_field:ui/elements/_wool
function color_field:render/set/set_blocks