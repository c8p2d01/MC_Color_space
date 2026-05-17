tellraw @a {"text":"[Color Field] UI","color":"green"}

# Cleaning
kill @e[type=marker,tag=ui_stillness_tracker]

kill @e[type=armor_stand,tag=movement_blocker]

# stop the momentum of the player
execute as @s at @s run summon armor_stand ~ ~ ~ {NoGravity:1b,Tags:["movement_blocker"]}

ride @s mount @e[tag=movement_blocker,limit=1,sort=nearest]

kill @e[type=armor_stand,tag=movement_blocker]

#track wether the player moved away
execute at @s run summon marker ~ ~ ~ {Tags:["ui_stillness_tracker"]}

tag @s add color_field_has_ui

# reset triggering mechanism
scoreboard players set @s click_wand 0

clear @p carrot_on_a_stick[custom_data={color_field:{ui_wand:true}}]

# running functions to summon UI elements at relative rotational positions (TODO)
# give all summoned UI elements this tag <tag=color_field_ui>

execute as @s at @s run function color_field:ui/sphere_markers
