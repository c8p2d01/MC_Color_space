import variables as var 
import math
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color
from coloraide import Color

def spherical_map(l, c, h, max_chroma):
    import math

    # normalize
    l = max(0.0, min(1.0, l))
    radius = min(c / max_chroma, 1.0) if max_chroma > 0 else 0.0

    # handle grayscale
    if c < 1e-6:
        theta = 0.0
    else:
        theta = h

    phi = (l - 0.5) * math.pi

    x = math.cos(theta) * math.cos(phi) * radius
    y = math.sin(phi)
    z = math.sin(theta) * math.cos(phi) * radius

    # map from [-1,1] → [0,CUBE]
    px = (x / 2) * var.CUBE_SIZE - var.HALF
    py = (y / 2) * var.CUBE_SIZE - var.HALF
    pz = (z / 2) * var.CUBE_SIZE - var.HALF

    return px, py, pz

def rgb_to_rgb(r, g, b):
    x = r * var.CUBE_SIZE - var.CUBE_SIZE
    y = g * var.CUBE_SIZE - var.CUBE_SIZE
    z = b * var.CUBE_SIZE - var.CUBE_SIZE
    return (x, y, z)

def rgb_to_hsl(r, g, b):
    color = Color("srgb", [r, g, b]).convert("hsl")
    h, s, l = color.coords()

    if h is None:
        h = 0.0

    theta = math.radians(h)

    radius = s

    x = math.cos(theta) * radius
    z = math.sin(theta) * radius
    y = l * 2 - 1

    if x != x:
        x = 0
    if y != y:
        y = 0
    if z != z:
        z = 0

    px = (x / 2) * var.CUBE_SIZE - var.HALF
    py = (y / 2) * var.CUBE_SIZE - var.HALF
    pz = (z / 2) * var.CUBE_SIZE - var.HALF

    return px, py, pz

def rgb_to_lab(r, g, b):
    rgb = sRGBColor(r, g, b, is_upscaled=False)
    lab = convert_color(rgb, LabColor)

    L = lab.lab_l
    a = lab.lab_a
    b_ = lab.lab_b

    # normalize
    x = a / 128.0
    y = (L / 100.0) * 2 - 1
    z = b_ / 128.0

    px = (x / 2) * var.CUBE_SIZE - var.HALF
    py = (y / 2) * var.CUBE_SIZE - var.HALF
    pz = (z / 2) * var.CUBE_SIZE - var.HALF

    return px, py, pz

def rgb_to_oklab(r, g, b):
    color = Color("srgb", [r, g, b]).convert("oklab")
    l, a, b_ = color.coords()

    # OKLab is already centered around 0
    x = a / 0.4     # scale to roughly [-1,1]
    y = l * 2 - 1
    z = b_ / 0.4

    px = (x / 2) * var.CUBE_SIZE - var.HALF
    py = (y / 2) * var.CUBE_SIZE - var.HALF
    pz = (z / 2) * var.CUBE_SIZE - var.HALF

    return px, py, pz

def rgb_to_oklch(r, g, b, MAX_CHROMA=0.37):
    import math
    from coloraide import Color

    color = Color("srgb", [r, g, b]).convert("oklch")
    l, c, h = color.coords()

    if h is None:
        h = 0.0

    theta = math.radians(h)

    return spherical_map(l, c, theta, MAX_CHROMA)