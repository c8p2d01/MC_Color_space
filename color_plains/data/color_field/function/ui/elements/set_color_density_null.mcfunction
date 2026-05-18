execute as @e[type=interaction,tag=layer_4,tag=yawstep_80] at @s run \
    summon text_display ^ ^ ^ {\
    Tags:["color_field","color_field_ui","transform_node"],\
    text:{"text":"None","color":"blue"},\
    billboard:"center",\
    brightness:{block:15,sky:15},\
    transformation:{\
        translation:[0f,0f,0f],\
        left_rotation:[0f,0f,0f,1f],\
        right_rotation:[0f,0f,0f,1f],\
        scale:[1.0f,1.0f,1.0f]\
    }\
}

tag @e[type=interaction,tag=layer_4,tag=yawstep_80,limit=1] add set_density_null