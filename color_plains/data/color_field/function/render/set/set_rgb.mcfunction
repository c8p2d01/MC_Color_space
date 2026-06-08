execute if score @s cf_coltype matches 0..7 run scoreboard players set @s cf_coltype 1
execute if score @s cf_coltype matches 8..15 run scoreboard players set @s cf_coltype 8

execute if score @s cf_feedback matches 1 run tellraw @s {"text":"rendering RGB Color Space","color":"green"}

execute as @a run function color_field:render/render