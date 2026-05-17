tellraw @a {"text":"[Color Field] Loaded","color":"green"}

scoreboard objectives add cf_cube dummy
scoreboard objectives add cf_density dummy
scoreboard objectives add cf_coltype dummy

execute as @a run scoreboard players set @s cf_coltype 4
execute as @a run function color_field:render/scale/scale_reset
execute as @a run function color_field:render/render

scoreboard objectives add click_wand minecraft.used:minecraft.carrot_on_a_stick

clear @p carrot_on_a_stick[custom_data={color_field:{ui_wand:true}}]
give @p carrot_on_a_stick[custom_data={color_field:{ui_wand:true}}] 1

