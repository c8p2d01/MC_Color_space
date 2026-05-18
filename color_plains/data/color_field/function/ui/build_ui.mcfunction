execute if score @s cf_feedback matches 1 run tellraw @a {"text":"[Color Field] UI","color":"green"}

# Cleaning
kill @e[type=marker,tag=ui_stillness_tracker]

kill @e[type=armor_stand,tag=movement_blocker]

# stop the momentum of the player

execute as @s at @s run summon armor_stand ~ ~-1.325 ~ {NoGravity:1b,Tags:["movement_blocker"]}

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

function color_field:ui/elements/toggle_feedback
function color_field:ui/elements/place_anchor
function color_field:ui/elements/toggle_render_anchor
function color_field:ui/elements/toggle_render_box
function color_field:ui/elements/set_rgb
function color_field:ui/elements/set_hsl
function color_field:ui/elements/set_lab
function color_field:ui/elements/set_oklab
function color_field:ui/elements/set_oklch
function color_field:ui/elements/set_color_density
function color_field:ui/elements/set_color_density_null
function color_field:ui/elements/set_color_density_fancy
function color_field:ui/elements/set_color_density_high
function color_field:ui/elements/set_color_density_mid
function color_field:ui/elements/set_color_density_low
