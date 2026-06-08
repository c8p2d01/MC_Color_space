from pathlib import Path

#
#   Important Folders
#

block_state_folder = f""
model_folder = f""
texture_folder = f""

#
#   Calculation
#

CUBE_SIZE = 12
RESOLUTION = 16
HALF = CUBE_SIZE / 2

#
#   File Creation
#

SCRIPT_DIR = Path(__file__).resolve().parent

#
#   UI distribution
#

LAYER_OFFSETS = [26, 15, -3, -20, -38]
AZIMUTH_STEP = 15  # degrees between markers around the vertical axis
RADIUS = 4.5         # distance from the executing entity

INTERACTION_HEIGHT = 0.7
INTERACTION_WIDTH = 0.7

UI_COUNT = (int)(360 / AZIMUTH_STEP) * len(LAYER_OFFSETS)



def validate_folders():
    folder_path = Path(texture_folder)

    if not folder_path.is_dir():
        raise FileNotFoundError(f"The required directory was not found: '{folder_path}'")

if __name__ == "__main__":
    pass
