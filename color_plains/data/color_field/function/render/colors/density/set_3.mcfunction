scoreboard players set @s cf_density 3

execute if score @s cf_coltype matches 8..15 run scoreboard players remove @s cf_coltype 7

execute as @s run kill @e[tag=ui_toggle_type]

execute as @s run function color_field:ui/elements/toggle_render_type

function color_field:render/render

