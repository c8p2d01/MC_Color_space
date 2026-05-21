execute if score @s cf_coltype matches 0..7 run scoreboard players add @s cf_coltype 21

execute if score @s cf_coltype matches 8..15 run scoreboard players remove @s cf_coltype 7

execute if score @s cf_coltype matches 21.. run scoreboard players remove @s cf_coltype 14

execute if score @s cf_feedback matches 1 run tellraw @a {"text":"toggled rendering type","color":"aqua"}

execute as @s run kill @e[tag=ui_toggle_type]

execute as @s run function color_field:ui/elements/toggle_render_type

function color_field:render/render
