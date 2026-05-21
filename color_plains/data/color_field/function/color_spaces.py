import variables as var
import color_conversion as colmath
import mc_writer
import math
import colorsys
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color
import random
from coloraide import Color

import math
import numpy as np

def generate_rgb(path):
    destination_4 = open(path, "w+")
    counter = 0;
    STEP = var.CUBE_SIZE / (var.RESOLUTION - 1)
    for x in range(var.RESOLUTION):
        for y in range(var.RESOLUTION):
            for z in range(var.RESOLUTION):
                r = int((x / (var.RESOLUTION - 1)) * 255)
                g = int((y / (var.RESOLUTION - 1)) * 255)
                b = int((z / (var.RESOLUTION - 1)) * 255)
                px = x * STEP
                py = y * STEP
                pz = z * STEP
                summon = mc_writer.create_summon_string_text(px, py, pz, r, g, b, 4, "rgb")
                destination_4.write(summon)
                counter += 1
    destination_4.close()

def generate_hsl(path):
    destination_4 = open(path, "w+")

    HUE_RESOLUTION = 24
    SATURATION_RESOLUTION = 12
    LIGHTNESS_RESOLUTION = 16

    FIELD_RADIUS = var.CUBE_SIZE / 2

    for h in range(HUE_RESOLUTION):
        theta = (h / HUE_RESOLUTION) * math.pi * 2
        for s in range(SATURATION_RESOLUTION):
            sat = s / (SATURATION_RESOLUTION - 1)
            radius = sat * FIELD_RADIUS
            for l in range(LIGHTNESS_RESOLUTION):
                light = l / (LIGHTNESS_RESOLUTION - 1)
                x = math.cos(theta) * radius + FIELD_RADIUS - var.HALF
                z = math.sin(theta) * radius + FIELD_RADIUS - var.HALF
                y = light * var.CUBE_SIZE - var.HALF
                r, g, b = colorsys.hls_to_rgb(
                    h / HUE_RESOLUTION,
                    light,
                    sat
                )
                r = int(r * 255)
                g = int(g * 255)
                b = int(b * 255)
                summon = mc_writer.create_summon_string_text(x, y, z, r, g, b, 4, "hsl")
                destination_4.write(summon)
    destination_4.close()

def generate_lab(path):
    destination_4=open(path,"w+")
    SAMPLES=6000
    for i in range(SAMPLES):
        x=(math.random() if hasattr(math,"random") else __import__("random").random())*2-1
        y=(math.random() if hasattr(math,"random") else __import__("random").random())*2-1
        z=(math.random() if hasattr(math,"random") else __import__("random").random())*2-1
        if x*x+y*y+z*z>1:
            continue
        px=x*var.HALF+var.HALF
        py=y*var.HALF+var.HALF
        pz=z*var.HALF+var.HALF
        L=(py/var.CUBE_SIZE)*100
        a=(px/var.CUBE_SIZE)*255-128
        b=(pz/var.CUBE_SIZE)*255-128
        lab=LabColor(lab_l=L,lab_a=a,lab_b=b)
        rgb=convert_color(lab,sRGBColor)
        r=max(0,min(255,int(rgb.clamped_rgb_r*255)))
        g=max(0,min(255,int(rgb.clamped_rgb_g*255)))
        b2=max(0,min(255,int(rgb.clamped_rgb_b*255)))
        s=mc_writer.create_summon_string_text(px,py,pz,r,g,b2,4, "lab")
        destination_4.write(s)
    destination_4.close()

def generate_oklab(path):
    destination_4=open(path,"w+")
    SAMPLES=6000
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
        px=((a/0.32)+1)*var.HALF
        py=l*var.CUBE_SIZE
        pz=((b/0.32)+1)*var.HALF
        s=mc_writer.create_summon_string_text(px,py,pz,r,g,b2,4, "oklab")
        destination_4.write(s)
    destination_4.close()

def generate_oklch(path):
    destination_4=open(path,"w+")
    MAX_CHROMA=0.37
    LIGHTNESS_STEPS=24
    HUE_STEPS=24
    CHROMA_STEPS=24
    RADIUS = var.CUBE_SIZE / 2
    for li in range(LIGHTNESS_STEPS):
        l=li/(LIGHTNESS_STEPS-1)
        py=l*var.CUBE_SIZE
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
                radius=(c/MAX_CHROMA)*RADIUS
                px=math.cos(theta)*radius+RADIUS
                pz=math.sin(theta)*radius+RADIUS
                s=mc_writer.create_summon_string_text(px,py,pz,r,g,b2,4, "oklch")
                destination_4.write(s)
    destination_4.close()

def classify_density(x, y, z):
    x *= 251
    y *= 257
    z *= 263
    h = (int(x) * 73856093) ^ (int(y) * 19349663) ^ (int(z) * 83492791)
    h = abs(h) % 15

    if h < 3:
        return 1          # ~3/15
    elif h < 9:
        return 2          # ~6/15
    else:
        return 3          # ~8/15

def generate(path, typ, densities, math):
    files = []
    for i in range(densities):
        f = open(path + "/" + typ + "/" + "density_" + str(i + 1) + ".mcfunction", "a")
        files.append(f)

    for x in range(var.RESOLUTION):
        for y in range(var.RESOLUTION):
            for z in range(var.RESOLUTION):
                r = x / var.RESOLUTION
                g = y / var.RESOLUTION
                b = z / var.RESOLUTION
                d = classify_density(r,g,b)

                px,py,pz = math(r,g,b)

                if (px != px):
                    px = var.HALF
                if (py != py):
                    py = var.HALF
                if (pz != pz):
                    pz = var.HALF

                summon = mc_writer.create_summon_string_text(px, py, pz, int(r*256), int(g*256), int(b*256), d, typ)
                if (d ==  1):
                    files[0].write(summon)
                elif (d ==  2):
                    files[1].write(summon)
                else:
                    files[2].write(summon)
    for f in files:
        f.close()
        
def generate_random(path, typ, mathfunc, fileno=4):
    f = open(path + "/" + typ + "/" + "density_" + str(fileno) + ".mcfunction", "w+")
    
    SAMPLES = 4000

    for s in range(SAMPLES):
        x = random.random()
        y = random.random()
        z = random.random()
        r = int(x * 255)
        g = int(y * 255)
        b = int(z * 255)
        px,py,pz = mathfunc(x,y,z)
        if (px != px):
            px = var.HALF
        if (py != py):
            py = var.HALF
        if (pz != pz):
            pz = var.HALF
        f.write(mc_writer.create_summon_string_text(px, py, pz, r, g, b, str(fileno), typ))
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
    reset_folder("render/colors/rgb", 3)
    reset_folder("render/colors/hsl", 3)
    reset_folder("render/colors/lab", 3)
    reset_folder("render/colors/oklab", 3)
    reset_folder("render/colors/oklch", 3)

if __name__ == "__main__":
    reset_files()
    generate("render/colors", "rgb", 3, colmath.rgb_to_rgb)
    generate_random("render/colors", "rgb", colmath.rgb_to_rgb, 4)
    generate("render/colors", "hsl", 3, colmath.rgb_to_hsl)
    generate_random("render/colors", "hsl", colmath.rgb_to_hsl, 4)
    generate("render/colors", "lab", 3, colmath.rgb_to_lab)
    generate_random("render/colors", "lab", colmath.rgb_to_lab, 4)
    generate("render/colors", "oklab", 3, colmath.rgb_to_oklab)
    generate_random("render/colors", "oklab", colmath.rgb_to_oklab, 4)
    generate("render/colors", "oklch", 3, colmath.rgb_to_oklch)
    generate_random("render/colors", "oklch", colmath.rgb_to_oklch, 4)