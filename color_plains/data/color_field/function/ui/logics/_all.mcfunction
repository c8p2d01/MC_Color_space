execute if score @s cf_block_all matches 1 run scoreboard players set @s cf_block_all 2
execute unless score @s cf_block_all matches 1..2 run scoreboard players set @s cf_block_all 1
execute if score @s cf_block_all matches 2 run scoreboard players set @s cf_block_all 0
execute as @s run kill @e[type=text_display,tag=ui_block_all]
execute as @s run function color_field:ui/elements/_all
function color_field:render/set/set_blocks