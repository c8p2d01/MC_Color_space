scoreboard players set @s cf_density 2

function color_field:render/render

tellraw @s {"text":"Density set to spotty","color":"green"}

function color_field:ui/set_style