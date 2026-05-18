scoreboard players set @s cf_coltype 4

function color_field:render/render

execute if score @s cf_feedback matches 1 run tellraw @s {"text":"rendering OKLAB Color Space","color":"green"}