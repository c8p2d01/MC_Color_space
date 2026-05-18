scoreboard players set @s cf_coltype 5

function color_field:render/render

execute if score @s cf_feedback matches 1 run tellraw @s {"text":"rendering OKLCH Color Space","color":"green"}