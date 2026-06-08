execute if score @s cf_coltype matches 0..7 run scoreboard players set @s cf_coltype 2
execute if score @s cf_coltype matches 8..15 run scoreboard players set @s cf_coltype 9

execute if score @s cf_feedback matches 1 run tellraw @s {"text":"rendering HSL Color Space","color":"green"}

function color_field:render/render