scoreboard players set @s cf_density 2

function color_field:render/render

execute if score @s cf_feedback matches 1 run tellraw @s {"text":"Density set to spotty","color":"green"}