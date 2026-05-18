# future:
# - anchor follow
# - display updates
# - color field rendering loop

# UI trigger
execute as @a[scores={click_wand=1..}] if items entity @s weapon.mainhand carrot_on_a_stick[custom_data={color_field:{ui_wand:true}}] run function color_field:ui/build_ui
# UI turn off triggger
execute as @e[tag=color_field_has_ui] at @s unless entity @e[type=marker,tag=ui_stillness_tracker,distance=..0.1] run function color_field:ui/clean_ui
# UI interactivity debug
execute as @e[type=interaction,tag=sphere_marker] if data entity @s interaction.player run function color_field:ui/click
# placement trigger
execute as @a[scores={click_wand=1..}] if items entity @s weapon.mainhand carrot_on_a_stick[custom_data={color_field:{render_wand:true}}] run function color_field:render/functions/place_anchor

#execute at @p run data modify entity @e[type=block_display,distance=..6] glowing set value 0b
#execute at @p run data modify entity @e[type=block_display,sort=nearest,limit=1,distance=..5] glowing set value 1b
