
import math
import colorsys
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color
import random
from coloraide import Color

def classify_density_rgb(x,y,z):
    v=((x*13)+(y*17)+(z*19))%16
    if v==0:
        return 1
    elif v<3:
        return 2
    elif v<7:
        return 3
    else:
        return 4

def classify_density_hsl(h,s,l):
    radial=int(s*12)
    angular=int((h/(math.pi*2))*48)
    vertical=int(l*16)
    v=((radial*7)+(angular*11)+(vertical*13))%16
    if v==0:
        return 1
    elif v<3:
        return 2
    elif v<7:
        return 3
    else:
        return 4

def classify_density_lab(l,a,b):
    radius=math.sqrt(a*a+b*b)
    angle=int((math.atan2(b,a)+math.pi)/(math.pi*2)*64)
    vertical=int(l)
    radial=int(radius)
    v=((vertical*5)+(radial*9)+(angle*13))%16
    if v==0:
        return 1
    elif v<3:
        return 2
    elif v<7:
        return 3
    else:
        return 4

def classify_density_oklab(l,a,b):
    radius=math.sqrt(a*a+b*b)
    angle=int((math.atan2(b,a)+math.pi)/(math.pi*2)*96)
    vertical=int(l*100)
    radial=int(radius*100)
    v=((vertical*3)+(radial*7)+(angle*11))%16
    if v==0:
        return 1
    elif v<3:
        return 2
    elif v<7:
        return 3
    else:
        return 4

def classify_density_oklch(l,c,h):
    vertical=int(l*100)
    radial=int(c*100)
    angular=int(h)
    spiral=int((angular+(vertical*2)+(radial*3))%128)
    v=((vertical*5)+(radial*7)+(spiral*11))%16
    if v==0:
        return 1
    elif v<3:
        return 2
    elif v<7:
        return 3
    else:
        return 4

def create_summon_string(x, y, z, r, g, b, d):
    return (
        f"execute as @e[type=marker,tag=color_field_anchor,limit=1] at @s run "\
        f"summon text_display ^{x} ^{y} ^{z} "\
        f"{{"\
        f"Tags:[\"color_field_space\",\"render_rgb\",\"density_{d}\"],"\
        f"billboard:\"center\","\
        f"text:{{\"text\":\"⬤\",\"color\":\"#{r:02x}{g:02x}{b:02x}\"}},"\
        f"background:0,"\
        f"transformation:{{"\
        f"left_rotation:[0f,0f,0f,1f],"\
        f"right_rotation:[0f,0f,0f,1f],"\
        f"translation:[0f,0f,0f],"\
        f"scale:[1.000f,1.000f,1.000f]}}"\
        f"}}\n"
    )

def generate_rgb():
    destination_1 = open("rgb/density_1.mcfunction", "a")
    destination_2 = open("rgb/density_2.mcfunction", "a")
    destination_3 = open("rgb/density_3.mcfunction", "a")
    destination_4 = open("rgb/density_4.mcfunction", "a")
    counter = 0;
    RESOLUTION = 16
    CUBE_SIZE = 8
    STEP = CUBE_SIZE / (RESOLUTION - 1)
    for x in range(RESOLUTION):
        for y in range(RESOLUTION):
            for z in range(RESOLUTION):
                r = int((x / (RESOLUTION - 1)) * 255)
                g = int((y / (RESOLUTION - 1)) * 255)
                b = int((z / (RESOLUTION - 1)) * 255)
                px = x * STEP
                py = y * STEP
                pz = z * STEP
                d=classify_density_rgb(r,g,b)
                if (d ==  1):
                    destination_1.write(create_summon_string(px, py, pz, r, g, b, d))
                elif (d ==  2):
                    destination_2.write(create_summon_string(x * STEP, y * STEP, z * STEP, r, g, b, d))
                elif (d ==  3):
                    destination_3.write(create_summon_string(x * STEP, y * STEP, z * STEP, r, g, b, d))
                else:
                    destination_4.write(create_summon_string(x * STEP, y * STEP, z * STEP, r, g, b, d))
                counter += 1
    destination_1.close()
    destination_2.close()
    destination_3.close()
    destination_4.close()

def generate_hsl():
    destination_1 = open("hsl/density_1.mcfunction", "a")
    destination_2 = open("hsl/density_2.mcfunction", "a")
    destination_3 = open("hsl/density_3.mcfunction", "a")
    destination_4 = open("hsl/density_4.mcfunction", "a")

    HUE_RESOLUTION = 48
    SATURATION_RESOLUTION = 12
    LIGHTNESS_RESOLUTION = 16

    FIELD_RADIUS = 4
    FIELD_HEIGHT = 8

    for h in range(HUE_RESOLUTION):
        theta = (h / HUE_RESOLUTION) * math.pi * 2
        for s in range(SATURATION_RESOLUTION):
            sat = s / (SATURATION_RESOLUTION - 1)
            radius = sat * FIELD_RADIUS
            for l in range(LIGHTNESS_RESOLUTION):
                light = l / (LIGHTNESS_RESOLUTION - 1)
                x = math.cos(theta) * radius + FIELD_RADIUS
                z = math.sin(theta) * radius + FIELD_RADIUS
                y = light * FIELD_HEIGHT
                r, g, b = colorsys.hls_to_rgb(
                    h / HUE_RESOLUTION,
                    light,
                    sat
                )
                r = int(r * 255)
                g = int(g * 255)
                b = int(b * 255)
                density = classify_density_hsl(h, s, l)
                summon = create_summon_string(x, y, z, r, g, b, density )

                if density == 1:
                    destination_1.write(summon)
                elif density == 2:
                    destination_2.write(summon)
                elif density == 3:
                    destination_3.write(summon)
                else:
                    destination_4.write(summon)
    destination_1.close()
    destination_2.close()
    destination_3.close()
    destination_4.close()

def generate_lab():
    destination_1=open("lab/density_1.mcfunction","a")
    destination_2=open("lab/density_2.mcfunction","a")
    destination_3=open("lab/density_3.mcfunction","a")
    destination_4=open("lab/density_4.mcfunction","a")
    RESOLUTION=24
    FIELD_SIZE=8
    HALF=FIELD_SIZE/2
    SAMPLES=6000
    for i in range(SAMPLES):
        x=(math.random() if hasattr(math,"random") else __import__("random").random())*2-1
        y=(math.random() if hasattr(math,"random") else __import__("random").random())*2-1
        z=(math.random() if hasattr(math,"random") else __import__("random").random())*2-1
        if x*x+y*y+z*z>1:
            continue
        px=x*HALF+HALF
        py=y*HALF+HALF
        pz=z*HALF+HALF
        L=(py/FIELD_SIZE)*100
        a=(px/FIELD_SIZE)*255-128
        b=(pz/FIELD_SIZE)*255-128
        lab=LabColor(lab_l=L,lab_a=a,lab_b=b)
        rgb=convert_color(lab,sRGBColor)
        r=max(0,min(255,int(rgb.clamped_rgb_r*255)))
        g=max(0,min(255,int(rgb.clamped_rgb_g*255)))
        b2=max(0,min(255,int(rgb.clamped_rgb_b*255)))
        d=classify_density_lab(int(px),int(py),int(pz))
        s=create_summon_string(px,py,pz,r,g,b2,d)
        if d==1:
            destination_1.write(s)
        elif d==2:
            destination_2.write(s)
        elif d==3:
            destination_3.write(s)
        else:
            destination_4.write(s)
    destination_1.close()
    destination_2.close()
    destination_3.close()
    destination_4.close()

def generate_oklab():
    destination_1=open("oklab/density_1.mcfunction","a")
    destination_2=open("oklab/density_2.mcfunction","a")
    destination_3=open("oklab/density_3.mcfunction","a")
    destination_4=open("oklab/density_4.mcfunction","a")
    FIELD_SIZE=8
    HALF=FIELD_SIZE/2
    SAMPLES=20000
    for i in range(SAMPLES):
        theta=random.random()*math.pi*2
        radius=(random.random()**0.5)*0.32
        light=random.random()
        a=math.cos(theta)*radius
        b=math.sin(theta)*radius
        l=light
        c=Color("oklab",[l,a,b]).convert("srgb")
        if not c.in_gamut():
            continue
        rgb=c.fit(method="clip").coords()
        r=max(0,min(255,int(rgb[0]*255)))
        g=max(0,min(255,int(rgb[1]*255)))
        b2=max(0,min(255,int(rgb[2]*255)))
        px=((a/0.32)+1)*HALF
        py=l*FIELD_SIZE
        pz=((b/0.32)+1)*HALF
        d=classify_density_oklab(int(px),int(py),int(pz))
        s=create_summon_string(px,py,pz,r,g,b2,d)
        if d==1:
            destination_1.write(s)
        elif d==2:
            destination_2.write(s)
        elif d==3:
            destination_3.write(s)
        else:
            destination_4.write(s)
    destination_1.close()
    destination_2.close()
    destination_3.close()
    destination_4.close()

def generate_oklch():
    destination_1=open("oklch/density_1.mcfunction","a")
    destination_2=open("oklch/density_2.mcfunction","a")
    destination_3=open("oklch/density_3.mcfunction","a")
    destination_4=open("oklch/density_4.mcfunction","a")
    HEIGHT=8
    MAX_CHROMA=0.37
    LIGHTNESS_STEPS=24
    HUE_STEPS=48
    CHROMA_STEPS=32
    for li in range(LIGHTNESS_STEPS):
        l=li/(LIGHTNESS_STEPS-1)
        py=l*HEIGHT
        chroma_limit=math.sin(l*math.pi)*MAX_CHROMA
        for hi in range(HUE_STEPS):
            h=(hi/HUE_STEPS)*360
            theta=math.radians(h)
            for ci in range(CHROMA_STEPS):
                c=(ci/(CHROMA_STEPS-1))*chroma_limit
                color=Color("oklch",[l,c,h])
                if not color.in_gamut("srgb"):
                    continue
                rgb=color.convert("srgb").fit(method="clip").coords()
                r=max(0,min(255,int(rgb[0]*255)))
                g=max(0,min(255,int(rgb[1]*255)))
                b2=max(0,min(255,int(rgb[2]*255)))
                radius=(c/MAX_CHROMA)*4
                px=math.cos(theta)*radius+4
                pz=math.sin(theta)*radius+4
                d=classify_density_oklch(li,ci,hi)
                s=create_summon_string(px,py,pz,r,g,b2,d)
                if d==1:
                    destination_1.write(s)
                elif d==2:
                    destination_2.write(s)
                elif d==3:
                    destination_3.write(s)
                else:
                    destination_4.write(s)
    destination_1.close()
    destination_2.close()
    destination_3.close()
    destination_4.close()

def reset_folder(dir, n):
    for i in range(n):
        file = open(f"{dir}/density_{i + 1}.mcfunction", "w+")
        if (i == 0):
            file.close()
            continue
        file.write(f"function color_field:render/{dir}/density_{i}\n")
        file.close()

def reset_files():
    reset_folder("rgb", 4)
    reset_folder("hsl", 4)
    reset_folder("lab", 4)
    reset_folder("oklab", 4)
    reset_folder("oklch", 4)

if __name__ == "__main__":
    reset_files()
    generate_rgb()
    generate_hsl()
    generate_lab()
    generate_oklab()
    generate_oklch()