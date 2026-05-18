execute as @e[type=interaction,tag=layer_0,tag=yawstep_320] at @s run \
    summon text_display ^ ^ ^ {\
    Tags:["color_field","color_field_ui","transform_node","render_rgb","density_1"],\
    text:{"text":"place\nAnchor","color":"gray"},\
    billboard:"center",\
    background:0,\
    brightness:{block:15,sky:15},\
    transformation:{\
        translation:[0f,0f,0f],\
        left_rotation:[0f,0f,0f,1f],\
        right_rotation:[0f,0f,0f,1f],\
        scale:[1.0f,1.0f,1.0f]\
    }\
}

tag @e[type=interaction,tag=layer_0,tag=yawstep_320,limit=1] add place_anchor
