tellraw @a {"text":"[Color Field] UI","color":"red"}

tag @p remove color_field_has_ui

execute at @s run kill @e[type=marker,tag=ui_stillness_tracker,sort=nearest,limit=1]

give @p carrot_on_a_stick[custom_data={color_field:{ui_wand:true}}] 1

kill @e[tag=color_field_ui]
