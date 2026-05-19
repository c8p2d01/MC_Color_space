tellraw @a {"text":"[Color Field] Loaded","color":"green"}

scoreboard objectives add cf_counter_node dummy
scoreboard objectives add cf_coltype dummy
scoreboard objectives add cf_density dummy
scoreboard objectives add cf_render_type dummy
scoreboard objectives add cf_feedback dummy

execute as @p run scoreboard players set @s cf_coltype 4
execute as @p run scoreboard players set @s cf_density 2
execute as @p run function color_field:render/render

scoreboard objectives add cf_block_stone dummy
scoreboard objectives add cf_block_light dummy
scoreboard objectives add cf_block_soil dummy
scoreboard objectives add cf_block_wood dummy
scoreboard objectives add cf_block_wool dummy
scoreboard objectives add cf_block_nether dummy
scoreboard objectives add cf_block_end dummy
scoreboard objectives add cf_block_ore dummy
scoreboard objectives add cf_block_utility dummy

execute as @p run scoreboard players set @s cf_block_stone 0
execute as @p run scoreboard players set @s cf_block_light 0
execute as @p run scoreboard players set @s cf_block_soil 0
execute as @p run scoreboard players set @s cf_block_wood 0
execute as @p run scoreboard players set @s cf_block_wool 0
execute as @p run scoreboard players set @s cf_block_nether 0
execute as @p run scoreboard players set @s cf_block_end 0
execute as @p run scoreboard players set @s cf_block_ore 0
execute as @p run scoreboard players set @s cf_block_utility 0

scoreboard objectives add click_wand minecraft.used:minecraft.carrot_on_a_stick
scoreboard objectives add place_wand minecraft.used:minecraft.carrot_on_a_stick

clear @p carrot_on_a_stick[custom_data={color_field:{ui_wand:true}}]
give @p carrot_on_a_stick[custom_data={color_field:{ui_wand:true}}] 1

