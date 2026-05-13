scoreboard players set @s cf_coltype 5

function color_field:render/render

tellraw @s {"text":"rendering OKLCH Color Space","color":"green"}

function color_field:ui/set_style