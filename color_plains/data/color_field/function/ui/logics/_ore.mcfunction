# toggle on

execute if score @s cf_block_ore matches 1 run scoreboard players set @s cf_block_ore 2

execute unless score @s cf_block_ore matches 1..2 run scoreboard players set @s cf_block_ore 1

execute if score @s cf_block_ore matches 2 run scoreboard players set @s cf_block_ore 0

function color_field:render/blocks/set
