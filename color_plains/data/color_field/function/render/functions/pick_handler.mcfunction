execute if score @s cf_feedback matches 1 run tellraw @a {"text":"Triggered picker","color":"green"}

execute as @s at @s run data modify storage color_field:main current_block set from entity @e[type=block_display,sort=nearest,limit=1,distance=..1] block_state.Name

execute if data storage color_field:main current_block if data entity @s interaction.player on target run function color_field:render/functions/give_macro with storage color_field:main

data remove entity @s interaction