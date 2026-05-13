# clear current render
function color_field:render/clear


#
#             RGB
#

# density 1
execute \
if score @s cf_coltype matches 1 \
if score @s cf_density matches 1 \
run function color_field:render/rgb/density_1

# density 2
execute \
if score @s cf_coltype matches 1 \
if score @s cf_density matches 2 \
run function color_field:render/rgb/density_2

# density 3
execute \
if score @s cf_coltype matches 1 \
if score @s cf_density matches 3 \
run function color_field:render/rgb/density_3

# density 4
execute \
if score @s cf_coltype matches 1 \
if score @s cf_density matches 4 \
run function color_field:render/rgb/density_4

#
#             HSL
#

# density 1
execute \
if score @s cf_coltype matches 2 \
if score @s cf_density matches 1 \
run function color_field:render/hsl/density_1

# density 2
execute \
if score @s cf_coltype matches 2 \
if score @s cf_density matches 2 \
run function color_field:render/hsl/density_2

# density 3
execute \
if score @s cf_coltype matches 2 \
if score @s cf_density matches 3 \
run function color_field:render/hsl/density_3

# density 4
execute \
if score @s cf_coltype matches 2 \
if score @s cf_density matches 4 \
run function color_field:render/hsl/density_4

#
#             LAB
#

# density 1
execute \
if score @s cf_coltype matches 3 \
if score @s cf_density matches 1 \
run function color_field:render/lab/density_1

# density 2
execute \
if score @s cf_coltype matches 3 \
if score @s cf_density matches 2 \
run function color_field:render/lab/density_2

# density 3
execute \
if score @s cf_coltype matches 3 \
if score @s cf_density matches 3 \
run function color_field:render/lab/density_3

# density 4
execute \
if score @s cf_coltype matches 3 \
if score @s cf_density matches 4 \
run function color_field:render/lab/density_4

#
#             OKLAB
#

# density 1
execute \
if score @s cf_coltype matches 4 \
if score @s cf_density matches 1 \
run function color_field:render/oklch/density_1

# density 2
execute \
if score @s cf_coltype matches 4 \
if score @s cf_density matches 2 \
run function color_field:render/oklab/density_2

# density 3
execute \
if score @s cf_coltype matches 4 \
if score @s cf_density matches 3 \
run function color_field:render/oklab/density_3

# density 4
execute \
if score @s cf_coltype matches 4 \
if score @s cf_density matches 4 \
run function color_field:render/oklab/density_4

#
#             OKLCH
#

# density 1
execute \
if score @s cf_coltype matches 5 \
if score @s cf_density matches 1 \
run function color_field:render/oklch/density_1

# density 2
execute \
if score @s cf_coltype matches 5 \
if score @s cf_density matches 2 \
run function color_field:render/oklch/density_2

# density 3
execute \
if score @s cf_coltype matches 5 \
if score @s cf_density matches 3 \
run function color_field:render/oklch/density_3

# density 4
execute \
if score @s cf_coltype matches 5 \
if score @s cf_density matches 4 \
run function color_field:render/oklch/density_4

tellraw @s {"text":"re rendered","color":"green"}