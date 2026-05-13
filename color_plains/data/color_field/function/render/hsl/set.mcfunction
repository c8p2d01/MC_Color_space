scoreboard players set @s cf_coltype 2

function color_field:render/render

tellraw @s {"text":"rendering HSL Color Space","color":"green"}

function color_field:ui/set_style