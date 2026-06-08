# MC_Color_space

## Introduction

MC_Color_space is a Minecraft datapack that brings interactive color space visualization into the game world. It allows players to render and explore various color models directly in Minecraft, making color theory tangible through block-based representations.

## Main Features

- **Color Space Rendering**: Visualize color fields in multiple color spaces including HSL, LAB, OKLAB, OKLCH, and RGB
- **Density Control**: Adjust rendering density with 4 levels (1-4) for different detail resolutions
- **Scaling System**: Dynamically scale the view with up/down/reset controls and clamping
- **Interactive UI**: Use an in-game book interface to configure settings and controls
- **Anchor Placement**: Position the color field anchor anywhere in the world

## Controls Summary

- **Book Interface**: Obtain and use the color control book to access UI functions for setting location, scale, style, and cover options
use /function color_field:give_book
- **Rendering**: Execute render commands to generate color fields based on selected parameters
- **Density**: Switch between density levels (1-4) for varying detail in color representations
- **Scaling**: Use scale commands to zoom in/out, reset, or apply scaling transformations (to the player)
- **Space Controls**: place the "anchor" of the visualisation anywhere if neede toggle the other corners as well
- **Clear**: Remove rendered color fields when needed

This datapack transforms Minecraft into a color exploration tool, perfect for artists, designers, and anyone interested in color theory.

## Version info

(26.1.2/vanilla)
default launcher (other launchers may run into issues with clickEvents)

the folder "color_plains" contains the actual datapack and needs to be moved as it is into the datapacks folder of your world

## Usage

within the functions folder and its subfolder you can find a few python scripts,
(Minecraft itself ignores all files withon a datapack which it cannot read so its ok to leave them there)

these files were used to generate the summoning commands used in this datapack

all other calculation is based on some things defined here, like the size of the display, but most importantly it defines the path of the texture files

the blocks displayed in this datapack are positioned using the original textures and models of the game
For running or changing these calculations the path to the respective folders needs to be defined by the user


<details>
<summary style="cursor: pointer;"><b>Variables</b></summary>

→ [file](./color_plains/data/color_field/function/variables.py)

all calculation is based on the original gamefiles. As i did not want to include and upload them myself you can use your own or find maintained repositories like this one https://github.com/PixiGeko/Minecraft-default-assets
In the file [variables.py](./color_plains/data/color_field/function/variables.py) you must define the path that applies to your system
there you can also adjust the base size of the visualisation Area

</details>

<details>
<summary style="cursor: pointer;"><b>Color Conversion</b></summary>

→ [file](./color_plains/data/color_field/function/color_conversion.py)

This file defines the functions i used to calculate the positions in the respective color fields as input i assumed x, y, and z to be rgb values in, each in range from 0 to 1

</details>

<details>
<summary style="cursor: pointer;"><b>Datapack Logic</b></summary>

→ [file](./color_plains/data/color_field/function/datapack_logic.py)

While some parts of this datapack can remain static, otheres are generated with scripts
this includes generating files to contoll those functionalities from the UserInterface.
This script defines functions used to do that. the files that need to be edited exist beforehand not as ".mcfunction" but as "_template", with their static parts being copied over and appended to with the generated functions.

</details>

### future challenges

place ingame textures at the appropiate position in the color spaces



