
import math
import colorsys
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color
import random
from coloraide import Color

CUBE_SIZE = 4

# def generate_lab():
#     destination_1=open("colors/lab/density_1.mcfunction","a")
#     destination_2=open("colors/lab/density_2.mcfunction","a")
#     destination_3=open("colors/lab/density_3.mcfunction","a")
#     destination_4=open("colors/lab/density_4.mcfunction","a")
#     RESOLUTION=24
#     HALF=CUBE_SIZE/2
#     SAMPLES=6000
#     for i in range(SAMPLES):
#         x=(math.random() if hasattr(math,"random") else __import__("random").random())*2-1
#         y=(math.random() if hasattr(math,"random") else __import__("random").random())*2-1
#         z=(math.random() if hasattr(math,"random") else __import__("random").random())*2-1
#         if x*x+y*y+z*z>1:
#             continue
#         px=x*HALF+HALF
#         py=y*HALF+HALF
#         pz=z*HALF+HALF
#         L=(py/CUBE_SIZE)*100
#         a=(px/CUBE_SIZE)*255-128
#         b=(pz/CUBE_SIZE)*255-128
#         lab=LabColor(lab_l=L,lab_a=a,lab_b=b)
#         rgb=convert_color(lab,sRGBColor)
#         r=max(0,min(255,int(rgb.clamped_rgb_r*255)))
#         g=max(0,min(255,int(rgb.clamped_rgb_g*255)))
#         b2=max(0,min(255,int(rgb.clamped_rgb_b*255)))
#         d=classify_density_lab(px / CUBE_SIZE, py / CUBE_SIZE, pz / CUBE_SIZE)
#         s=create_summon_string(px,py,pz,r,g,b2,d, "lab")
#         if d==1:
#             destination_1.write(s)
#         elif d==2:
#             destination_2.write(s)
#         elif d==3:
#             destination_3.write(s)
#         else:
#             destination_4.write(s)
#     destination_1.close()
#     destination_2.close()
#     destination_3.close()
#     destination_4.close()

# def generate_oklab():
#     destination_1=open("colors/oklab/density_1.mcfunction","a")
#     destination_2=open("colors/oklab/density_2.mcfunction","a")
#     destination_3=open("colors/oklab/density_3.mcfunction","a")
#     destination_4=open("colors/oklab/density_4.mcfunction","a")
#     HALF=CUBE_SIZE/2
#     SAMPLES=20000
#     for i in range(SAMPLES):
#         theta=random.random()*math.pi*2
#         radius=(random.random()**0.5)*0.32
#         light=random.random()
#         a=math.cos(theta)*radius
#         b=math.sin(theta)*radius
#         l=light
#         c=Color("oklab",[l,a,b]).convert("srgb")
#         if not c.in_gamut():
#             continue
#         rgb=c.fit(method="clip").coords()
#         r=max(0,min(255,int(rgb[0]*255)))
#         g=max(0,min(255,int(rgb[1]*255)))
#         b2=max(0,min(255,int(rgb[2]*255)))
#         px=((a/0.32)+1)*HALF
#         py=l*CUBE_SIZE
#         pz=((b/0.32)+1)*HALF
#         d=classify_density_oklab(px / CUBE_SIZE, py / CUBE_SIZE, pz / CUBE_SIZE)
#         s=create_summon_string(px,py,pz,r,g,b2,d, "oklab")
#         if d==1:
#             destination_1.write(s)
#         elif d==2:
#             destination_2.write(s)
#         elif d==3:
#             destination_3.write(s)
#         else:
#             destination_4.write(s)
#     destination_1.close()
#     destination_2.close()
#     destination_3.close()
#     destination_4.close()

# def generate_oklch():
#     destination_1=open("colors/oklch/density_1.mcfunction","a")
#     destination_2=open("colors/oklch/density_2.mcfunction","a")
#     destination_3=open("colors/oklch/density_3.mcfunction","a")
#     destination_4=open("colors/oklch/density_4.mcfunction","a")
#     MAX_CHROMA=0.37
#     LIGHTNESS_STEPS=24
#     HUE_STEPS=24
#     CHROMA_STEPS=24
#     RADIUS = CUBE_SIZE / 2
#     for li in range(LIGHTNESS_STEPS):
#         l=li/(LIGHTNESS_STEPS-1)
#         py=l*CUBE_SIZE
#         chroma_limit=math.sin(l*math.pi)*MAX_CHROMA
#         for hi in range(HUE_STEPS):
#             h=(hi/HUE_STEPS)*360
#             theta=math.radians(h)
#             for ci in range(CHROMA_STEPS):
#                 c=(ci/(CHROMA_STEPS-1))*chroma_limit
#                 color=Color("oklch",[l,c,h])
#                 if not color.in_gamut("srgb"):
#                     continue
#                 rgb=color.convert("srgb").fit(method="clip").coords()
#                 r=max(0,min(255,int(rgb[0]*255)))
#                 g=max(0,min(255,int(rgb[1]*255)))
#                 b2=max(0,min(255,int(rgb[2]*255)))

#                 phi=(l-0.5)*math.pi
#                 radius=(c/MAX_CHROMA)*RADIUS

#                 px=math.cos(theta)*math.cos(phi)*radius+RADIUS
#                 py=math.sin(phi)*RADIUS+RADIUS
#                 pz=math.sin(theta)*math.cos(phi)*radius+RADIUS
#                 d=classify_density_oklch(li,ci,hi)
#                 s=create_summon_string(px,py,pz,r,g,b2,d, "oklch")
#                 if d==1:
#                     destination_1.write(s)
#                 elif d==2:
#                     destination_2.write(s)
#                 elif d==3:
#                     destination_3.write(s)
#                 else:
#                     destination_4.write(s)
#     destination_1.close()
#     destination_2.close()
#     destination_3.close()
#     destination_4.close()
























































CUBE_SIZE = 4
RESOLUTION = 16
HALF = CUBE_SIZE / 2

def classify_density(x, y, z):
    h = (x * 73856093) ^ (y * 19349663) ^ (z * 83492791)
    h = abs(h) % 15

    if h == 0:
        return 1          # ~1/15
    elif h < 3:
        return 2          # ~2/15
    elif h < 7:
        return 3          # ~4/15
    else:
        return 4          # ~8/15

# ,\"spinBlock\"

def create_summon_string(x, y, z, r, g, b, d, type):
    return (\
        f"execute as @e[tag=color_field_anchor,limit=1] at @s run summon text_display "\
        f"~{(x - CUBE_SIZE / 2):.4f} ~{(y - CUBE_SIZE / 2):.4f} ~{(z - CUBE_SIZE / 2):.4f} {{"\
        f"Tags:[\"color_field\",\"color_field_node\",\"render_{type}\",\"density_{d}\"],"\
        f"text:{{\"text\":\"⬤\",\"color\":\"#{r:02x}{g:02x}{b:02x}\"}},"\
        f"background:0,"\
        f"brightness:{{block:15,sky:15}},"\
        f"billboard:\"center\","\
        f"transformation:{{"\
        f"translation:[0f,0f,0f],"\
        f"left_rotation:[0f,0f,0f,1f],"\
        f"right_rotation:[0f,0f,0f,1f],"\
        f"scale:[{CUBE_SIZE / 4}f,{CUBE_SIZE / 4}f,{CUBE_SIZE / 4}f]"\
        f"}}"\
        f"}}\n"\
    )

def rgb_to_rgb(r, g, b):
    x = r / (RESOLUTION * CUBE_SIZE)
    y = g / (RESOLUTION * CUBE_SIZE)
    z = b / (RESOLUTION * CUBE_SIZE)
    return (x, y, z)

def rgb_to_hsl(r, g, b):
    rgb = [r/255, g/255, b/255]
    px, py, pz = 0, 0, 0

    color = Color("srgb", rgb).convert("hsl")
    h, s, l = color.coords()  # NOTE: order is (h, s, l)

    theta = math.radians(h)

    radius = s

    px = math.cos(theta) * radius * HALF + HALF
    py = l * CUBE_SIZE
    pz = math.sin(theta) * radius * HALF + HALF

    return px, py, pz

def rgb_to_lab(r, g, b2, MAX_CHROMA=128):
    rgb_color = sRGBColor(r / 255.0, g / 255.0, b2 / 255.0)
    lab = convert_color(rgb_color, LabColor)
    L = lab.lab_l
    a = lab.lab_a
    b = lab.lab_b
    
    y = (L / 100.0) * 2 - 1
    x = ((a + 128) / 255.0) * 2 - 1
    z = ((b + 128) / 255.0) * 2 - 1
    
    # if x*x + y*y + z*z > 1:
    #     continue
        
    px = x * HALF + HALF
    py = y * HALF + HALF
    pz = z * HALF + HALF
    return px, py, pz

def rgb_to_oklab(r, g, b, MAX_CHROMA=0.32):
    rgb = [r/255, g/255, b/255]
    px, py, pz = 0, 0, 0

    color = Color("srgb", rgb).convert("oklab")
    l, a, b_ = color.coords()

    # polar conversion (like OKLCH internally)
    c = math.sqrt(a*a + b_*b_)
    h = math.atan2(b_, a)

    theta = h  # already radians

    phi = (l - 0.5) * math.pi
    radius = c / MAX_CHROMA

    px = math.cos(theta) * math.cos(phi) * radius * HALF + HALF
    py = math.sin(phi) * HALF + HALF
    pz = math.sin(theta) * math.cos(phi) * radius * HALF + HALF

    return px, py, pz

def rgb_to_oklch(r, g, b, CUBE_SIZE=8, MAX_CHROMA=0.37):
    # normalize RGB
    rgb = [r/255, g/255, b/255]

    # convert to OKLCH
    color = Color("srgb", rgb).convert("oklch")
    l, c, h = color.coords()

    # handle undefined hue (grays)
    if h is None:
        h = 0.0

    theta = math.radians(h)

    # spherical mapping
    phi = (l - 0.5) * math.pi
    radius = c / MAX_CHROMA

    HALF = CUBE_SIZE / 2

    px = math.cos(theta) * math.cos(phi) * radius * HALF + HALF
    py = math.sin(phi) * HALF + HALF
    pz = math.sin(theta) * math.cos(phi) * radius * HALF + HALF

    return px, py, pz

def generate(path, typ, densities, math):
    files = []
    for i in range(densities):
        f = open(path + "/" + typ + "/" + "density_" + str(i + 1) + ".mcfunction", "a")
        files.append(f)

    STEP = CUBE_SIZE / (RESOLUTION - 1)
    for x in range(RESOLUTION):
        for y in range(RESOLUTION):
            for z in range(RESOLUTION):
                r = int((x / (RESOLUTION - 1)) * 255)
                g = int((y / (RESOLUTION - 1)) * 255)
                b = int((z / (RESOLUTION - 1)) * 255)
                d = classify_density(r,g,b)

                px,py,pz = math(r,g,b)

                if (px != px):
                    px = HALF
                if (py != py):
                    py = HALF
                if (pz != pz):
                    pz = HALF

                summon = create_summon_string(px, py, pz, r, g, b, d, typ)
                if (d ==  1):
                    files[0].write(summon)
                elif (d ==  2):
                    files[1].write(summon)
                elif (d ==  3):
                    files[2].write(summon)
                else:
                    files[3].write(summon)
    for f in files:
        f.close()

def reset_folder(dir, n):
    for i in range(n):
        file = open(f"{dir}/density_{i + 1}.mcfunction", "w+")
        if (i == 0):
            file.close()
            continue
        file.write(f"function color_field:render/{dir}/density_{i}\n")
        file.close()

def reset_files():
    reset_folder("colors/rgb", 4)
    reset_folder("colors/hsl", 4)
    reset_folder("colors/lab", 4)
    reset_folder("colors/oklab", 4)
    reset_folder("colors/oklch", 4)

if __name__ == "__main__":
    reset_files()
    generate("colors", "rgb", 4, rgb_to_rgb)
    generate("colors", "hsl", 4, rgb_to_hsl)
    generate("colors", "lab", 4, rgb_to_lab)
    generate("colors", "oklab", 4, rgb_to_oklab)
    generate("colors", "oklch", 4, rgb_to_oklch)