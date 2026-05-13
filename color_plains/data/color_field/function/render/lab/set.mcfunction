scoreboard players set @s cf_coltype 3

function color_field:render/render

tellraw @s {"text":"rendering LAB Color Space","color":"green"}

function color_field:ui/set_style