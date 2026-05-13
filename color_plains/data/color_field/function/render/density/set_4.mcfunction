scoreboard players set @s cf_density 4

function color_field:render/render

tellraw @s {"text":"Density set to full","color":"green"}

function color_field:ui/set_style