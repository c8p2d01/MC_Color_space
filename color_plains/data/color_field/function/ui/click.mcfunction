# debugging interaction

execute if score @s cf_feedback matches 1 run tellraw @a [{"text":"Tags of the clicked Entity: "},{"nbt":"Tags","entity":"@s","color":"yellow"}]

execute if entity @s[tag=place_anchor] if data entity @s interaction.player on target run function color_field:ui/logics/place_anchor
execute if entity @s[tag=toggle_render_anchor] if data entity @s interaction.player on target run function color_field:ui/logics/toggle_render_anchor
execute if entity @s[tag=toggle_render_box] if data entity @s interaction.player on target run function color_field:ui/logics/toggle_render_box
execute if entity @s[tag=toggle_feedback] if data entity @s interaction.player on target run function color_field:ui/logics/toggle_feedback

execute if entity @s[tag=set_rgb] if data entity @s interaction.player on target run function color_field:render/colors/rgb/set
execute if entity @s[tag=set_hsl] if data entity @s interaction.player on target run function color_field:render/colors/hsl/set
execute if entity @s[tag=set_lab] if data entity @s interaction.player on target run function color_field:render/colors/lab/set
execute if entity @s[tag=set_oklab] if data entity @s interaction.player on target run function color_field:render/colors/oklab/set
execute if entity @s[tag=set_oklch] if data entity @s interaction.player on target run function color_field:render/colors/oklch/set
execute if entity @s[tag=set_density_null] if data entity @s interaction.player on target run kill @e[type=text_display,tag=color_field_node]
execute if entity @s[tag=set_density_fancy] if data entity @s interaction.player on target run function color_field:render/colors/density/set_4
execute if entity @s[tag=set_density_high] if data entity @s interaction.player on target run function color_field:render/colors/density/set_3
execute if entity @s[tag=set_density_mid] if data entity @s interaction.player on target run function color_field:render/colors/density/set_2
execute if entity @s[tag=set_density_low] if data entity @s interaction.player on target run function color_field:render/colors/density/set_1

data remove entity @s interaction

