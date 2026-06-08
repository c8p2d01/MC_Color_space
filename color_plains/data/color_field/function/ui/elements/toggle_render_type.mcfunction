execute if score @s cf_coltype matches 0..7 as @e[type=interaction,tag=layer_1,tag=yawstep_345] at @s run \
    summon text_display ^ ^ ^ {\
    Tags:["color_field","color_field_ui","ui_toggle_type"],\
    text:{"text":"Show\nBlocks","color":"auqa"},\
    billboard:"center",\
    brightness:{block:15,sky:15},\
    transformation:{\
        translation:[0f,0f,0f],\
        left_rotation:[0f,0f,0f,1f],\
        right_rotation:[0f,0f,0f,1f],\
        scale:[1.0f,1.0f,1.0f]\
    }\
}

execute if score @s cf_coltype matches 0..7 run tag @e[type=interaction,tag=layer_1,tag=yawstep_345,limit=1] add toggle_render_type
execute if score @s cf_coltype matches 0..7 run tag @e[type=interaction,tag=layer_1,tag=yawstep_30,limit=1] remove toggle_render_type

execute if score @s cf_coltype matches 8..15 as @e[type=interaction,tag=layer_1,tag=yawstep_30] at @s run \
    summon text_display ^ ^ ^ {\
    Tags:["color_field","color_field_ui","ui_toggle_type"],\
    text:{"text":"Show\nColors","color":"aqua"},\
    billboard:"center",\
    brightness:{block:15,sky:15},\
    transformation:{\
        translation:[0f,0f,0f],\
        left_rotation:[0f,0f,0f,1f],\
        right_rotation:[0f,0f,0f,1f],\
        scale:[1.0f,1.0f,1.0f]\
    }\
}

execute if score @s cf_coltype matches 8..15 run tag @e[type=interaction,tag=layer_1,tag=yawstep_30,limit=1] add toggle_render_type
execute if score @s cf_coltype matches 8..15 run tag @e[type=interaction,tag=layer_1,tag=yawstep_345,limit=1] remove toggle_render_type
