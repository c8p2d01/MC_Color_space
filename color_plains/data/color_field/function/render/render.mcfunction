# clear current render

function color_field:render/clear

execute if score @s cf_feedback matches 1 run tellraw @s {"text":"re rendered","color":"green"}

#
#             RGB
#

execute \
if score @s cf_coltype matches 1 \
if score @s cf_density matches 1 \
run function color_field:render/colors/rgb/density_1

# density 1
execute \
if score @s cf_coltype matches 1 \
if score @s cf_density matches 1 \
run function color_field:render/colors/rgb/density_1

# density 2
execute \
if score @s cf_coltype matches 1 \
if score @s cf_density matches 2 \
run function color_field:render/colors/rgb/density_2

# density 3
execute \
if score @s cf_coltype matches 1 \
if score @s cf_density matches 3 \
run function color_field:render/colors/rgb/density_3

# density 4
execute \
if score @s cf_coltype matches 1 \
if score @s cf_density matches 4 \
run function color_field:render/colors/rgb/density_4

#
#             HSL
#

# density 1
execute \
if score @s cf_coltype matches 2 \
if score @s cf_density matches 1 \
run function color_field:render/colors/hsl/density_1

# density 2
execute \
if score @s cf_coltype matches 2 \
if score @s cf_density matches 2 \
run function color_field:render/colors/hsl/density_2

# density 3
execute \
if score @s cf_coltype matches 2 \
if score @s cf_density matches 3 \
run function color_field:render/colors/hsl/density_3

# density 4
execute \
if score @s cf_coltype matches 2 \
if score @s cf_density matches 4 \
run function color_field:render/colors/hsl/density_4

#
#             LAB
#

# density 1
execute \
if score @s cf_coltype matches 3 \
if score @s cf_density matches 1 \
run function color_field:render/colors/lab/density_1

# density 2
execute \
if score @s cf_coltype matches 3 \
if score @s cf_density matches 2 \
run function color_field:render/colors/lab/density_2

# density 3
execute \
if score @s cf_coltype matches 3 \
if score @s cf_density matches 3 \
run function color_field:render/colors/lab/density_3

# density 4
execute \
if score @s cf_coltype matches 3 \
if score @s cf_density matches 4 \
run function color_field:render/colors/lab/density_4

#
#             OKLAB
#

# density 1
execute \
if score @s cf_coltype matches 4 \
if score @s cf_density matches 1 \
run function color_field:render/colors/oklab/density_1

# density 2
execute \
if score @s cf_coltype matches 4 \
if score @s cf_density matches 2 \
run function color_field:render/colors/oklab/density_2

# density 3
execute \
if score @s cf_coltype matches 4 \
if score @s cf_density matches 3 \
run function color_field:render/colors/oklab/density_3

# density 4
execute \
if score @s cf_coltype matches 4 \
if score @s cf_density matches 4 \
run function color_field:render/colors/oklab/density_4

#
#             OKLCH
#

# density 1
execute \
if score @s cf_coltype matches 5 \
if score @s cf_density matches 1 \
run function color_field:render/colors/oklch/density_1

# density 2
execute \
if score @s cf_coltype matches 5 \
if score @s cf_density matches 2 \
run function color_field:render/colors/oklch/density_2

# density 3
execute \
if score @s cf_coltype matches 5 \
if score @s cf_density matches 3 \
run function color_field:render/colors/oklch/density_3

# density 4
execute \
if score @s cf_coltype matches 5 \
if score @s cf_density matches 4 \
run function color_field:render/colors/oklch/density_4

#
#             Blocks
#

# wood
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_wood matches 1 \
run function color_field:render/blocks/rgb/wood
execute \
if score @s cf_coltype matches 9 \
if score @s cf_block_wood matches 1 \
run function color_field:render/blocks/hsl/wood
execute \
if score @s cf_coltype matches 10 \
if score @s cf_block_wood matches 1 \
run function color_field:render/blocks/lab/wood
execute \
if score @s cf_coltype matches 11 \
if score @s cf_block_wood matches 1 \
run function color_field:render/blocks/oklab/wood
execute \
if score @s cf_coltype matches 12 \
if score @s cf_block_wood matches 1 \
run function color_field:render/blocks/oklch/wood

# utility
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_utility matches 1 \
run function color_field:render/blocks/rgb/utility
execute \
if score @s cf_coltype matches 9 \
if score @s cf_block_utility matches 1 \
run function color_field:render/blocks/hsl/utility
execute \
if score @s cf_coltype matches 10 \
if score @s cf_block_utility matches 1 \
run function color_field:render/blocks/lab/utility
execute \
if score @s cf_coltype matches 11 \
if score @s cf_block_utility matches 1 \
run function color_field:render/blocks/oklab/utility
execute \
if score @s cf_coltype matches 12 \
if score @s cf_block_utility matches 1 \
run function color_field:render/blocks/oklch/utility

# misc
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_misc matches 1 \
run function color_field:render/blocks/rgb/misc
execute \
if score @s cf_coltype matches 9 \
if score @s cf_block_misc matches 1 \
run function color_field:render/blocks/hsl/misc
execute \
if score @s cf_coltype matches 10 \
if score @s cf_block_misc matches 1 \
run function color_field:render/blocks/lab/misc
execute \
if score @s cf_coltype matches 11 \
if score @s cf_block_misc matches 1 \
run function color_field:render/blocks/oklab/misc
execute \
if score @s cf_coltype matches 12 \
if score @s cf_block_misc matches 1 \
run function color_field:render/blocks/oklch/misc

# ore
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_ore matches 1 \
run function color_field:render/blocks/rgb/ore
execute \
if score @s cf_coltype matches 9 \
if score @s cf_block_ore matches 1 \
run function color_field:render/blocks/hsl/ore
execute \
if score @s cf_coltype matches 10 \
if score @s cf_block_ore matches 1 \
run function color_field:render/blocks/lab/ore
execute \
if score @s cf_coltype matches 11 \
if score @s cf_block_ore matches 1 \
run function color_field:render/blocks/oklab/ore
execute \
if score @s cf_coltype matches 12 \
if score @s cf_block_ore matches 1 \
run function color_field:render/blocks/oklch/ore

# stone
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_stone matches 1 \
run function color_field:render/blocks/rgb/stone
execute \
if score @s cf_coltype matches 9 \
if score @s cf_block_stone matches 1 \
run function color_field:render/blocks/hsl/stone
execute \
if score @s cf_coltype matches 10 \
if score @s cf_block_stone matches 1 \
run function color_field:render/blocks/lab/stone
execute \
if score @s cf_coltype matches 11 \
if score @s cf_block_stone matches 1 \
run function color_field:render/blocks/oklab/stone
execute \
if score @s cf_coltype matches 12 \
if score @s cf_block_stone matches 1 \
run function color_field:render/blocks/oklch/stone

# crops
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_crops matches 1 \
run function color_field:render/blocks/rgb/crops
execute \
if score @s cf_coltype matches 9 \
if score @s cf_block_crops matches 1 \
run function color_field:render/blocks/hsl/crops
execute \
if score @s cf_coltype matches 10 \
if score @s cf_block_crops matches 1 \
run function color_field:render/blocks/lab/crops
execute \
if score @s cf_coltype matches 11 \
if score @s cf_block_crops matches 1 \
run function color_field:render/blocks/oklab/crops
execute \
if score @s cf_coltype matches 12 \
if score @s cf_block_crops matches 1 \
run function color_field:render/blocks/oklch/crops

# wool
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_wool matches 1 \
run function color_field:render/blocks/rgb/wool
execute \
if score @s cf_coltype matches 9 \
if score @s cf_block_wool matches 1 \
run function color_field:render/blocks/hsl/wool
execute \
if score @s cf_coltype matches 10 \
if score @s cf_block_wool matches 1 \
run function color_field:render/blocks/lab/wool
execute \
if score @s cf_coltype matches 11 \
if score @s cf_block_wool matches 1 \
run function color_field:render/blocks/oklab/wool
execute \
if score @s cf_coltype matches 12 \
if score @s cf_block_wool matches 1 \
run function color_field:render/blocks/oklch/wool

# light
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_light matches 1 \
run function color_field:render/blocks/rgb/light
execute \
if score @s cf_coltype matches 9 \
if score @s cf_block_light matches 1 \
run function color_field:render/blocks/hsl/light
execute \
if score @s cf_coltype matches 10 \
if score @s cf_block_light matches 1 \
run function color_field:render/blocks/lab/light
execute \
if score @s cf_coltype matches 11 \
if score @s cf_block_light matches 1 \
run function color_field:render/blocks/oklab/light
execute \
if score @s cf_coltype matches 12 \
if score @s cf_block_light matches 1 \
run function color_field:render/blocks/oklch/light

# concrete
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_concrete matches 1 \
run function color_field:render/blocks/rgb/concrete
execute \
if score @s cf_coltype matches 9 \
if score @s cf_block_concrete matches 1 \
run function color_field:render/blocks/hsl/concrete
execute \
if score @s cf_coltype matches 10 \
if score @s cf_block_concrete matches 1 \
run function color_field:render/blocks/lab/concrete
execute \
if score @s cf_coltype matches 11 \
if score @s cf_block_concrete matches 1 \
run function color_field:render/blocks/oklab/concrete
execute \
if score @s cf_coltype matches 12 \
if score @s cf_block_concrete matches 1 \
run function color_field:render/blocks/oklch/concrete

# concrete_powder
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_concrete_powder matches 1 \
run function color_field:render/blocks/rgb/concrete_powder
execute \
if score @s cf_coltype matches 9 \
if score @s cf_block_concrete_powder matches 1 \
run function color_field:render/blocks/hsl/concrete_powder
execute \
if score @s cf_coltype matches 10 \
if score @s cf_block_concrete_powder matches 1 \
run function color_field:render/blocks/lab/concrete_powder
execute \
if score @s cf_coltype matches 11 \
if score @s cf_block_concrete_powder matches 1 \
run function color_field:render/blocks/oklab/concrete_powder
execute \
if score @s cf_coltype matches 12 \
if score @s cf_block_concrete_powder matches 1 \
run function color_field:render/blocks/oklch/concrete_powder

# terracotta
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_terracotta matches 1 \
run function color_field:render/blocks/rgb/terracotta
execute \
if score @s cf_coltype matches 9 \
if score @s cf_block_terracotta matches 1 \
run function color_field:render/blocks/hsl/terracotta
execute \
if score @s cf_coltype matches 10 \
if score @s cf_block_terracotta matches 1 \
run function color_field:render/blocks/lab/terracotta
execute \
if score @s cf_coltype matches 11 \
if score @s cf_block_terracotta matches 1 \
run function color_field:render/blocks/oklab/terracotta
execute \
if score @s cf_coltype matches 12 \
if score @s cf_block_terracotta matches 1 \
run function color_field:render/blocks/oklch/terracotta

# glass
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_glass matches 1 \
run function color_field:render/blocks/rgb/glass
execute \
if score @s cf_coltype matches 9 \
if score @s cf_block_glass matches 1 \
run function color_field:render/blocks/hsl/glass
execute \
if score @s cf_coltype matches 10 \
if score @s cf_block_glass matches 1 \
run function color_field:render/blocks/lab/glass
execute \
if score @s cf_coltype matches 11 \
if score @s cf_block_glass matches 1 \
run function color_field:render/blocks/oklab/glass
execute \
if score @s cf_coltype matches 12 \
if score @s cf_block_glass matches 1 \
run function color_field:render/blocks/oklch/glass

# ice
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_ice matches 1 \
run function color_field:render/blocks/rgb/ice
execute \
if score @s cf_coltype matches 9 \
if score @s cf_block_ice matches 1 \
run function color_field:render/blocks/hsl/ice
execute \
if score @s cf_coltype matches 10 \
if score @s cf_block_ice matches 1 \
run function color_field:render/blocks/lab/ice
execute \
if score @s cf_coltype matches 11 \
if score @s cf_block_ice matches 1 \
run function color_field:render/blocks/oklab/ice
execute \
if score @s cf_coltype matches 12 \
if score @s cf_block_ice matches 1 \
run function color_field:render/blocks/oklch/ice

# block
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_block matches 1 \
run function color_field:render/blocks/rgb/block
execute \
if score @s cf_coltype matches 9 \
if score @s cf_block_block matches 1 \
run function color_field:render/blocks/hsl/block
execute \
if score @s cf_coltype matches 10 \
if score @s cf_block_block matches 1 \
run function color_field:render/blocks/lab/block
execute \
if score @s cf_coltype matches 11 \
if score @s cf_block_block matches 1 \
run function color_field:render/blocks/oklab/block
execute \
if score @s cf_coltype matches 12 \
if score @s cf_block_block matches 1 \
run function color_field:render/blocks/oklch/block

# coral
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_coral matches 1 \
run function color_field:render/blocks/rgb/coral
execute \
if score @s cf_coltype matches 9 \
if score @s cf_block_coral matches 1 \
run function color_field:render/blocks/hsl/coral
execute \
if score @s cf_coltype matches 10 \
if score @s cf_block_coral matches 1 \
run function color_field:render/blocks/lab/coral
execute \
if score @s cf_coltype matches 11 \
if score @s cf_block_coral matches 1 \
run function color_field:render/blocks/oklab/coral
execute \
if score @s cf_coltype matches 12 \
if score @s cf_block_coral matches 1 \
run function color_field:render/blocks/oklch/coral

# sculk
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_sculk matches 1 \
run function color_field:render/blocks/rgb/sculk
execute \
if score @s cf_coltype matches 9 \
if score @s cf_block_sculk matches 1 \
run function color_field:render/blocks/hsl/sculk
execute \
if score @s cf_coltype matches 10 \
if score @s cf_block_sculk matches 1 \
run function color_field:render/blocks/lab/sculk
execute \
if score @s cf_coltype matches 11 \
if score @s cf_block_sculk matches 1 \
run function color_field:render/blocks/oklab/sculk
execute \
if score @s cf_coltype matches 12 \
if score @s cf_block_sculk matches 1 \
run function color_field:render/blocks/oklch/sculk

# creative
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_creative matches 1 \
run function color_field:render/blocks/rgb/creative
execute \
if score @s cf_coltype matches 9 \
if score @s cf_block_creative matches 1 \
run function color_field:render/blocks/hsl/creative
execute \
if score @s cf_coltype matches 10 \
if score @s cf_block_creative matches 1 \
run function color_field:render/blocks/lab/creative
execute \
if score @s cf_coltype matches 11 \
if score @s cf_block_creative matches 1 \
run function color_field:render/blocks/oklab/creative
execute \
if score @s cf_coltype matches 12 \
if score @s cf_block_creative matches 1 \
run function color_field:render/blocks/oklch/creative

# dirt
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_dirt matches 1 \
run function color_field:render/blocks/rgb/dirt
execute \
if score @s cf_coltype matches 9 \
if score @s cf_block_dirt matches 1 \
run function color_field:render/blocks/hsl/dirt
execute \
if score @s cf_coltype matches 10 \
if score @s cf_block_dirt matches 1 \
run function color_field:render/blocks/lab/dirt
execute \
if score @s cf_coltype matches 11 \
if score @s cf_block_dirt matches 1 \
run function color_field:render/blocks/oklab/dirt
execute \
if score @s cf_coltype matches 12 \
if score @s cf_block_dirt matches 1 \
run function color_field:render/blocks/oklch/dirt

execute as @e[tag=color_field_anchor,limit=1] at @s run summon interaction ~ ~ ~ {Tags:["color_field","block_shifter"],width:0.125f,height:0.125f}

execute store result score #count cf_counter_node if score @s cf_coltype matches 0..7 run execute if entity @e[type=text_display,tag=color_field_node]

execute store result score #count cf_counter_node if score @s cf_coltype matches 8..15 run execute if entity @e[type=block_display,tag=color_field_block]

execute if score @s cf_feedback matches 1 run tellraw @a [{"text":"[ColorField] ","color":"dark_aqua","bold":true},{"text":"Number of active Nodes","color":"green"},{"score":{"name":"#count","objective":"cf_counter_node"},"color":"gold","bold":true}]
