# ----------------------------------------
# CLEAN OLD CUBE
# ----------------------------------------

kill @e[type=text_display,tag=color_field_cube]

# ensure rotation consistency
function color_field:render/space/update_rotation

# ----------------------------------------
# CUBE CORNERS (LOCAL SPACE)
# ----------------------------------------

# 000
execute as @e[type=marker,tag=color_field_anchor,limit=1] at @s run \
summon text_display ^0 ^0 ^0 \
{\
    Tags:["color_field_cube"],\
    billboard:"center",\
    text:{"text":"⬤","color":"#000000"},\
    background:0,\
    transformation:{\
        left_rotation:[0f,0f,0f,1f],\
        right_rotation:[0f,0f,0f,1f],\
        translation:[0f,0f,0f],\
        scale:[1f,1f,1f]\
    }\
}

# 100
execute as @e[type=marker,tag=color_field_anchor,limit=1] at @s run \
summon text_display ^8 ^0 ^0 \
{\
    Tags:["color_field_cube"],\
    billboard:"center",\
    text:{"text":"⬤","color":"#000000"},\
    background:0,\
    transformation:{\
        left_rotation:[0f,0f,0f,1f],\
        right_rotation:[0f,0f,0f,1f],\
        translation:[0f,0f,0f],\
        scale:[1f,1f,1f]\
    }\
}

# 010
execute as @e[type=marker,tag=color_field_anchor,limit=1] at @s run \
summon text_display ^0 ^8 ^0 \
{\
    Tags:["color_field_cube"],\
    billboard:"center",\
    text:{"text":"⬤","color":"#000000"},\
    background:0,\
    transformation:{\
        left_rotation:[0f,0f,0f,1f],\
        right_rotation:[0f,0f,0f,1f],\
        translation:[0f,0f,0f],\
        scale:[1f,1f,1f]\
    }\
}

# 110
execute as @e[type=marker,tag=color_field_anchor,limit=1] at @s run \
summon text_display ^8 ^8 ^0 \
{\
    Tags:["color_field_cube"],\
    billboard:"center",\
    text:{"text":"⬤","color":"#000000"},\
    background:0,\
    transformation:{\
        left_rotation:[0f,0f,0f,1f],\
        right_rotation:[0f,0f,0f,1f],\
        translation:[0f,0f,0f],\
        scale:[1f,1f,1f]\
    }\
}

# 001
execute as @e[type=marker,tag=color_field_anchor,limit=1] at @s run \
summon text_display ^0 ^0 ^8 \
{\
    Tags:["color_field_cube"],\
    billboard:"center",\
    text:{"text":"⬤","color":"#000000"},\
    background:0,\
    transformation:{\
        left_rotation:[0f,0f,0f,1f],\
        right_rotation:[0f,0f,0f,1f],\
        translation:[0f,0f,0f],\
        scale:[1f,1f,1f]\
    }\
}

# 101
execute as @e[type=marker,tag=color_field_anchor,limit=1] at @s run \
summon text_display ^8 ^0 ^8 \
{\
    Tags:["color_field_cube"],\
    billboard:"center",\
    text:{"text":"⬤","color":"#000000"},\
    background:0,\
    transformation:{\
        left_rotation:[0f,0f,0f,1f],\
        right_rotation:[0f,0f,0f,1f],\
        translation:[0f,0f,0f],\
        scale:[1f,1f,1f]\
    }\
}

# 011
execute as @e[type=marker,tag=color_field_anchor,limit=1] at @s run \
summon text_display ^0 ^8 ^8 \
{\
    Tags:["color_field_cube"],\
    billboard:"center",\
    text:{"text":"⬤","color":"#000000"},\
    background:0,\
    transformation:{\
        left_rotation:[0f,0f,0f,1f],\
        right_rotation:[0f,0f,0f,1f],\
        translation:[0f,0f,0f],\
        scale:[1f,1f,1f]\
    }\
}

# 111
execute as @e[type=marker,tag=color_field_anchor,limit=1] at @s run \
summon text_display ^8 ^8 ^8 \
{\
    Tags:["color_field_cube"],\
    billboard:"center",\
    text:{"text":"⬤","color":"#000000"},\
    background:0,\
    transformation:{\
        left_rotation:[0f,0f,0f,1f],\
        right_rotation:[0f,0f,0f,1f],\
        translation:[0f,0f,0f],\
        scale:[1f,1f,1f]\
    }\
}

