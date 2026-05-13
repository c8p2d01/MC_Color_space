tellraw @a {"text":"[Color Field] Loaded","color":"green"}

scoreboard objectives add cf_scale dummy
scoreboard objectives add cf_book_page dummy
scoreboard objectives add cf_cube dummy
scoreboard objectives add cf_density dummy
scoreboard objectives add cf_coltype dummy

execute as @a run scoreboard players set @s cf_density 2
execute as @a run scoreboard players set @s cf_book_page 0
execute as @a run scoreboard players set @s cf_coltype 4
execute as @a run function color_field:render/scale/scale_reset
execute as @a run function color_field:render/render
execute as @a run function color_field:give_book