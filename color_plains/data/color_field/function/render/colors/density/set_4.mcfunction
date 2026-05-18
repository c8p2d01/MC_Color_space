scoreboard players set @s cf_density 4

function color_field:render/render

execute if score @s cf_feedback matches 1 run tellraw @s {"text":"Density set to full","color":"green"}