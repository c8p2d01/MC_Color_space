# clear current render

function color_field:render/clear

execute if score @s cf_feedback matches 1 run tellraw @s {"text":"re rendered","color":"green"}

execute store result score #count cf_counter_node run execute if entity @e[type=text_display,tag=color_field_node]

execute if score @s cf_feedback matches 1 run tellraw @a [{"text":"[ColorField] ","color":"dark_aqua","bold":true},{"text":"Number of active Nodes","color":"green"},{"score":{"name":"#count","objective":"cf_counter_node"},"color":"gold","bold":true}]

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
run function color_field:render/blocks/wood

# utility
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_utility matches 1 \
run function color_field:render/blocks/utility

# misc
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_misc matches 1 \
run function color_field:render/blocks/misc

# ore
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_ore matches 1 \
run function color_field:render/blocks/ore

# stone
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_stone matches 1 \
run function color_field:render/blocks/stone

# crops
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_crops matches 1 \
run function color_field:render/blocks/crops

# wool
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_wool matches 1 \
run function color_field:render/blocks/wool

# light
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_light matches 1 \
run function color_field:render/blocks/light

# concrete
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_concrete matches 1 \
run function color_field:render/blocks/concrete

# concrete_powder
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_concrete_powder matches 1 \
run function color_field:render/blocks/concrete_powder

# terracotta
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_terracotta matches 1 \
run function color_field:render/blocks/terracotta

# glass
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_glass matches 1 \
run function color_field:render/blocks/glass

# ice
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_ice matches 1 \
run function color_field:render/blocks/ice

# block
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_block matches 1 \
run function color_field:render/blocks/block

# coral
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_coral matches 1 \
run function color_field:render/blocks/coral

# sculk
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_sculk matches 1 \
run function color_field:render/blocks/sculk

# creative
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_creative matches 1 \
run function color_field:render/blocks/creative

# dirt
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_dirt matches 1 \
run function color_field:render/blocks/dirt

execute as @e[tag=color_field_anchor,limit=1] at @s run summon interaction ~ ~ ~ {Tags:["color_field","block_shifter"],width:0.125f,height:0.125f}