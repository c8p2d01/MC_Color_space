execute as @e[tag=color_field_anchor,limit=1] at @s run \
    summon block_display ~ ~0.5 ~0.5 {\
    Tags:["color_field_block"],\
    block_state:{Name:"minecraft:stone"}\
    }

