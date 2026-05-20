tellraw @a {"text":"[Color Field] Loaded","color":"green"}

scoreboard objectives add cf_counter_node dummy
scoreboard objectives add cf_coltype dummy
scoreboard objectives add cf_density dummy
scoreboard objectives add cf_render_type dummy
scoreboard objectives add cf_feedback dummy

execute as @p run scoreboard players set @s cf_coltype 4
execute as @p run scoreboard players set @s cf_density 2
execute as @p run function color_field:render/render

scoreboard objectives add click_wand minecraft.used:minecraft.carrot_on_a_stick
scoreboard objectives add place_wand minecraft.used:minecraft.carrot_on_a_stick

clear @p carrot_on_a_stick[custom_data={color_field:{ui_wand:true}}]
give @p carrot_on_a_stick[custom_data={color_field:{ui_wand:true}}] 1

scoreboard objectives add cf_block_wood dummy
execute as @p run scoreboard players set @s cf_block_wood 0
scoreboard objectives add cf_block_utility dummy
execute as @p run scoreboard players set @s cf_block_utility 0
scoreboard objectives add cf_block_misc dummy
execute as @p run scoreboard players set @s cf_block_misc 0
scoreboard objectives add cf_block_ore dummy
execute as @p run scoreboard players set @s cf_block_ore 0
scoreboard objectives add cf_block_stone dummy
execute as @p run scoreboard players set @s cf_block_stone 0
scoreboard objectives add cf_block_crops dummy
execute as @p run scoreboard players set @s cf_block_crops 0
scoreboard objectives add cf_block_wool dummy
execute as @p run scoreboard players set @s cf_block_wool 0
scoreboard objectives add cf_block_light dummy
execute as @p run scoreboard players set @s cf_block_light 0
scoreboard objectives add cf_block_concrete dummy
execute as @p run scoreboard players set @s cf_block_concrete 0
scoreboard objectives add cf_block_concrete_powder dummy
execute as @p run scoreboard players set @s cf_block_concrete_powder 0
scoreboard objectives add cf_block_terracotta dummy
execute as @p run scoreboard players set @s cf_block_terracotta 0
scoreboard objectives add cf_block_glass dummy
execute as @p run scoreboard players set @s cf_block_glass 0
scoreboard objectives add cf_block_ice dummy
execute as @p run scoreboard players set @s cf_block_ice 0
scoreboard objectives add cf_block_block dummy
execute as @p run scoreboard players set @s cf_block_block 0
scoreboard objectives add cf_block_coral dummy
execute as @p run scoreboard players set @s cf_block_coral 0
scoreboard objectives add cf_block_sculk dummy
execute as @p run scoreboard players set @s cf_block_sculk 0
scoreboard objectives add cf_block_creative dummy
execute as @p run scoreboard players set @s cf_block_creative 0
scoreboard objectives add cf_block_dirt dummy
execute as @p run scoreboard players set @s cf_block_dirt 0
