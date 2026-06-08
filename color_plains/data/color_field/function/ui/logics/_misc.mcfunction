execute if score @s cf_block_misc matches 1 run scoreboard players set @s cf_block_misc 2
execute unless score @s cf_block_misc matches 1..2 run scoreboard players set @s cf_block_misc 1
execute if score @s cf_block_misc matches 2 run scoreboard players set @s cf_block_misc 0
execute as @s run kill @e[type=text_display,tag=ui_block_misc]
execute as @s run function color_field:ui/elements/_misc
function color_field:render/set/set_blocks