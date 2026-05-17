import math

# Layers: center (eye level), then ±17° and ±34° from eye level
LAYER_OFFSETS = [30, 15, -3, -20, -38]
AZIMUTH_STEP = 20  # degrees between markers around the vertical axis
RADIUS = 4.5         # distance from the executing entity
OUTPUT_FILE = "sphere_markers.mcfunction"


def compile_markers():
    commands = []

    for layer_idx, pitch_deg in enumerate(LAYER_OFFSETS):
        for yaw_deg in range(0, 360, AZIMUTH_STEP):
            # Tags include yaw step relative to the executor and the layer index
            tags = f'"color_field_ui","sphere_marker","yawstep_{yaw_deg}","layer_{layer_idx}"'
            nbt = '{' + 'Tags:[' + tags + ']}'

            # Use relative rotation and caret coordinates so markers are positioned
            # at a distance RADIUS from the executor, rotated by the executor's yaw
            # plus the yaw step and pitched by the layer angle.
            cmd = f"execute at @s rotated ~{yaw_deg} {pitch_deg} run summon interaction ^ ^ ^{RADIUS} " + nbt
            commands.append(cmd)

    return commands


if __name__ == "__main__":
    marker_commands = compile_markers()
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out_file:
        out_file.write("\n".join(marker_commands) + "\n")

    print(f"Generated {len(marker_commands)} marker summon commands in {OUTPUT_FILE}")
