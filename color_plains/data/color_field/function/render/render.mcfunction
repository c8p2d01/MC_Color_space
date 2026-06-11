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

# all
execute \
if score @s cf_coltype matches 8 \
if score @s cf_block_all matches 1 \
run function color_field:render/blocks/rgb/all
execute \
if score @s cf_coltype matches 9 \
if score @s cf_block_all matches 1 \
run function color_field:render/blocks/hsl/all
execute \
if score @s cf_coltype matches 10 \
if score @s cf_block_all matches 1 \
run function color_field:render/blocks/lab/all
execute \
if score @s cf_coltype matches 11 \
if score @s cf_block_all matches 1 \
run function color_field:render/blocks/oklab/all
execute \
if score @s cf_coltype matches 12 \
if score @s cf_block_all matches 1 \
run function color_field:render/blocks/oklch/all

execute as @e[tag=color_field_anchor,limit=1] at @s run summon interaction ~ ~ ~ {Tags:["color_field","block_shifter"],width:0.375f,height:0.375f}

execute store result score #count cf_counter_node if score @s cf_coltype matches 0..7 run execute if entity @e[type=text_display,tag=color_field_node]

execute store result score #count cf_counter_node if score @s cf_coltype matches 8..15 run execute if entity @e[type=block_display,tag=color_field_block]

execute if score @s cf_feedback matches 1 run tellraw @a [{"text":"[ColorField] ","color":"dark_aqua","bold":true},{"text":"Number of active Nodes","color":"green"},{"score":{"name":"#count","objective":"cf_counter_node"},"color":"gold","bold":true}]
