scoreboard players set @s cf_density 1

function color_field:render/render

execute if score @s cf_feedback matches 1 run tellraw @s {"text":"Density set to sparse","color":"green"}