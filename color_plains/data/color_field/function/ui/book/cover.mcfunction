clear @s written_book[custom_data={color_field:{ui_book:true}}]

give @s written_book\
[\
    custom_data={color_field:{ui_book:true}},\
    written_book_content=\
    {\
        title:"Color Field",author:"system",pages:\
        [\
            [\
                {\
                    "text":"X","color":"gray","bold":false,"click_event":\
                    {\
                        "action":"run_command",command:"/function color_field:ui/set_cover"\
                    }\
                }\
                ,{\
                    "text":"\n   Color Spaces\n","color":"gold","bold":true\
                }\
                ,{\
                    "text":"\n\n     created by","color":"gray","bold":false\
                }\
                ,{\
                    "text":"\n\n       Valaritas","color":"dark_purple","bold":false\
                }\
                ,{\
                    "text":"\n\n     inspired by\n\n","color":"gray","bold":false\
                }\
                ,{\
                    "text":"       ","color":"gray","bold":false\
                }\
                ,{\
                    "text":"Gneiss","color":"dark_green","bold":false, "underlined":true,"click_event":\
                    {\
                        "action":"open_url",url:"https://youtu.be/nJlZT5AE9zY"\
                    }\
                }\
            ]\
            ,[\
                {\
                    "text":"Pick Rendering style\n\n","color":"black","bold":true\
                }\
                ,{\
                    "text":"RGB\n","color":"dark_gray","bold":false,"underlined":true,"click_event":\
                    {\
                        "action":"run_command",command:"/function color_field:render/rgb/set"\
                    }\
                }\
                ,{\
                    "text":"HSL\n","color":"dark_gray","bold":false,"underlined":true,"click_event":\
                    {\
                        "action":"run_command",command:"/function color_field:render/hsl/set"\
                    }\
                }\
                ,{\
                    "text":"LAB\n","color":"dark_gray","bold":false,"underlined":true,"click_event":\
                    {\
                        "action":"run_command",command:"/function color_field:render/lab/set"\
                    }\
                }\
                ,{\
                    "text":"OKLAB\n","color":"dark_gray","bold":false,"underlined":true,"click_event":\
                    {\
                        "action":"run_command",command:"/function color_field:render/oklab/set"\
                    }\
                }\
                ,{\
                    "text":"OKLCH\n","color":"dark_gray","bold":false,"underlined":true,"click_event":\
                    {\
                        "action":"run_command",command:"/function color_field:render/oklch/set"\
                    }\
                }\
                ,{\
                    "text":"\nnode density\n","color":"black","bold":false\
                }\
                ,{\
                    "text":"full\n","color":"blue","bold":false,"underlined":true,"click_event":\
                    {\
                        "action":"run_command",command:"/function color_field:render/density/set_4"\
                    }\
                }\
                ,{\
                    "text":"medium\n","color":"aqua","bold":false,"underlined":true,"click_event":\
                    {\
                        "action":"run_command",command:"/function color_field:render/density/set_3"\
                    }\
                }\
                ,{\
                    "text":"spotty\n","color":"green","bold":false,"underlined":true,"click_event":\
                    {\
                        "action":"run_command",command:"/function color_field:render/density/set_2"\
                    }\
                }\
                ,{\
                    "text":"sparse\n","color":"dark_green","bold":false,"underlined":true,"click_event":\
                    {\
                        "action":"run_command",command:"/function color_field:render/density/set_1"\
                    }\
                }\
            ]\
            ,[\
                {\
                    "text":"change Location of Visulalisation\n","color":"black","bold":false\
                }\
                ,{\
                    "text":"\nplace Anchor\n","color":"dark_green","bold":false,"underlined":true,"click_event":\
                    {\
                        "action":"run_command",command:"/function color_field:render/space/anchor_place"\
                    }\
                }\
                ,{\
                    "text":"\nrender corners\n","color":"dark_aqua","bold":false,"underlined":true,"click_event":\
                    {\
                        "action":"run_command",command:"/function color_field:render/space/cube_toggle"\
                    }\
                }\
            ]\
            ,[\
                {\
                    "text":"Viewing Scale\n","color":"black","bold":false\
                }\
                ,{\
                    "text":"change scale of the player\n","color":"gray","bold":false\
                }\
                ,{\
                    "text":"\nscale reset\n","color":"dark_gray","underlined":true,"click_event":\
                    {\
                        "action":"run_command",command:"/function color_field:render/scale/scale_reset"\
                    }\
                }\
                ,{\
                    "text":"\nscale up\n","color":"dark_gray","underlined":true,"click_event":\
                    {\
                        "action":"run_command",command:"/function color_field:render/scale/scale_up"\
                    }\
                }\
                ,{\
                    "text":"\nscale down\n","color":"dark_gray","underlined":true,"click_event":\
                    {\
                        "action":"run_command",command:"/function color_field:render/scale/scale_down"\
                    }\
                }\
                ,{\
                    "text":"\nwe scale the player instead of re calculating all positions","color":"gray","bold":false\
                }\
            ]\
        ]\
    }\
]
