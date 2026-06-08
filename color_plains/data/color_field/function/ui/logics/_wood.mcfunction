execute if score @s cf_block_wood matches 1 run scoreboard players set @s cf_block_wood 2
execute unless score @s cf_block_wood matches 1..2 run scoreboard players set @s cf_block_wood 1
execute if score @s cf_block_wood matches 2 run scoreboard players set @s cf_block_wood 0
execute as @s run kill @e[type=text_display,tag=ui_block_wood]
execute as @s run function color_field:ui/elements/_wood
function color_field:render/set/set_blocks