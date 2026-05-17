scoreboard players set @s cf_density 3

function color_field:render/render

tellraw @s {"text":"Density set to medium","color":"green"}
