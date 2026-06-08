# toggle on

execute if score @s cf_feedback matches 1 run scoreboard players set @s cf_feedback 2

execute unless score @s cf_feedback matches 1..2 run scoreboard players set @s cf_feedback 1

execute if score @s cf_feedback matches 2 run scoreboard players set @s cf_feedback 0

execute if score @s cf_feedback matches 1 run tellraw @a {"text":"toggled UI feedback on","color":"aqua"}
execute if score @s cf_feedback matches 0 run tellraw @a {"text":"toggled UI feedback off","color":"light_purple"}
