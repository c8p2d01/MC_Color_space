scoreboard players set @s cf_density 1

function color_field:render/render

tellraw @s {"text":"Density set to sparse","color":"green"}

function color_field:ui/set_style