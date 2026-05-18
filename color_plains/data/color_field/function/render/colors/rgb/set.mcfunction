scoreboard players set @s cf_coltype 1

execute as @a run function color_field:render/render

execute if score @s cf_feedback matches 1 run tellraw @s {"text":"rendering RGB Color Space","color":"green"}