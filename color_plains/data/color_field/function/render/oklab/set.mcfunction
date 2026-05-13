scoreboard players set @s cf_coltype 4

function color_field:render/render

tellraw @s {"text":"rendering OKLAB Color Space","color":"green"}

function color_field:ui/set_style