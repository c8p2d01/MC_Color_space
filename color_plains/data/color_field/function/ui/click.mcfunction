# debugging interaction

execute if score @s cf_feedback matches 1 run tellraw @a [{"text":"Tags of the clicked Entity: "},{"nbt":"Tags","entity":"@s","color":"yellow"}]

execute if entity @s[tag=place_anchor] if data entity @s interaction.player on target run function color_field:ui/logics/place_anchor
execute if entity @s[tag=toggle_render_anchor] if data entity @s interaction.player on target run function color_field:ui/logics/toggle_render_anchor
execute if entity @s[tag=toggle_render_box] if data entity @s interaction.player on target run function color_field:ui/logics/toggle_render_box
execute if entity @s[tag=toggle_feedback] if data entity @s interaction.player on target run function color_field:ui/logics/toggle_feedback
execute if entity @s[tag=toggle_render_type] if data entity @s interaction.player on target run function color_field:ui/logics/toggle_render_type

execute if entity @s[tag=set_rgb] if data entity @s interaction.player on target run function color_field:render/set/set_rgb
execute if entity @s[tag=set_hsl] if data entity @s interaction.player on target run function color_field:render/set/set_hsl
execute if entity @s[tag=set_lab] if data entity @s interaction.player on target run function color_field:render/set/set_lab
execute if entity @s[tag=set_oklab] if data entity @s interaction.player on target run function color_field:render/set/set_oklab
execute if entity @s[tag=set_oklch] if data entity @s interaction.player on target run function color_field:render/set/set_oklch
execute if entity @s[tag=set_density_null] if data entity @s interaction.player on target run kill @e[type=text_display,tag=color_field_node]
execute if entity @s[tag=set_density_fancy] if data entity @s interaction.player on target run function color_field:render/colors/density/set_4
execute if entity @s[tag=set_density_high] if data entity @s interaction.player on target run function color_field:render/colors/density/set_3
execute if entity @s[tag=set_density_mid] if data entity @s interaction.player on target run function color_field:render/colors/density/set_2
execute if entity @s[tag=set_density_low] if data entity @s interaction.player on target run function color_field:render/colors/density/set_1

execute if entity @s[tag=toggle_wood] if data entity @s interaction.player on target run function color_field:ui/logics/_wood
execute if entity @s[tag=toggle_utility] if data entity @s interaction.player on target run function color_field:ui/logics/_utility
execute if entity @s[tag=toggle_misc] if data entity @s interaction.player on target run function color_field:ui/logics/_misc
execute if entity @s[tag=toggle_ore] if data entity @s interaction.player on target run function color_field:ui/logics/_ore
execute if entity @s[tag=toggle_stone] if data entity @s interaction.player on target run function color_field:ui/logics/_stone
execute if entity @s[tag=toggle_crops] if data entity @s interaction.player on target run function color_field:ui/logics/_crops
execute if entity @s[tag=toggle_wool] if data entity @s interaction.player on target run function color_field:ui/logics/_wool
execute if entity @s[tag=toggle_light] if data entity @s interaction.player on target run function color_field:ui/logics/_light
execute if entity @s[tag=toggle_concrete] if data entity @s interaction.player on target run function color_field:ui/logics/_concrete
execute if entity @s[tag=toggle_concrete_powder] if data entity @s interaction.player on target run function color_field:ui/logics/_concrete_powder
execute if entity @s[tag=toggle_terracotta] if data entity @s interaction.player on target run function color_field:ui/logics/_terracotta
execute if entity @s[tag=toggle_glass] if data entity @s interaction.player on target run function color_field:ui/logics/_glass
execute if entity @s[tag=toggle_ice] if data entity @s interaction.player on target run function color_field:ui/logics/_ice
execute if entity @s[tag=toggle_block] if data entity @s interaction.player on target run function color_field:ui/logics/_block
execute if entity @s[tag=toggle_coral] if data entity @s interaction.player on target run function color_field:ui/logics/_coral
execute if entity @s[tag=toggle_sculk] if data entity @s interaction.player on target run function color_field:ui/logics/_sculk
execute if entity @s[tag=toggle_creative] if data entity @s interaction.player on target run function color_field:ui/logics/_creative
execute if entity @s[tag=toggle_dirt] if data entity @s interaction.player on target run function color_field:ui/logics/_dirt

data remove entity @s interaction
