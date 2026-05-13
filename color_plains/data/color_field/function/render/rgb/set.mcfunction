scoreboard players set @s cf_coltype 1

function color_field:render/render

tellraw @s {"text":"rendering RGB Color Space","color":"green"}

function color_field:ui/set_style