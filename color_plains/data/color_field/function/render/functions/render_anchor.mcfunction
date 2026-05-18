# anchor visual
execute at @e[type=marker,tag=color_field_anchor,limit=1] run summon text_display ~ ~ ~ \
{\
    Tags:["color_field","color_field_anchor_visual"],\
    billboard:"center",\
    text:{"text":"⬤","color":"#0d0d0d"},\
    background:0,\
    transformation:{\
        left_rotation:[0f,0f,0f,1f],\
        right_rotation:[0f,0f,0f,1f],\
        translation:[0f,0f,0f],\
        scale:[2f,2f,2f]\
    }\
}