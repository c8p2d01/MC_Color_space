execute if score @s cf_coltype matches 0..7 run scoreboard players set @s cf_coltype 3
execute if score @s cf_coltype matches 8..15 run scoreboard players set @s cf_coltype 10

execute if score @s cf_feedback matches 1 run tellraw @s {"text":"rendering LAB Color Space","color":"green"}

function color_field:render/render