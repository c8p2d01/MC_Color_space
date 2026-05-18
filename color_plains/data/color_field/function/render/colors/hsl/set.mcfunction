scoreboard players set @s cf_coltype 2

function color_field:render/render

execute if score @s cf_feedback matches 1 run tellraw @s {"text":"rendering HSL Color Space","color":"green"}