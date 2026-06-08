execute if score @s cf_block_dirt matches 1 run scoreboard players set @s cf_block_dirt 2
execute unless score @s cf_block_dirt matches 1..2 run scoreboard players set @s cf_block_dirt 1
execute if score @s cf_block_dirt matches 2 run scoreboard players set @s cf_block_dirt 0
execute as @s run kill @e[type=text_display,tag=ui_block_dirt]
execute as @s run function color_field:ui/elements/_dirt
function color_field:render/set/set_blocks