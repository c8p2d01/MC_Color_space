# toggle on

execute if score @s cf_block_wool matches 1 run scoreboard players set @s cf_block_wool 2

execute unless score @s cf_block_wool matches 1..2 run scoreboard players set @s cf_block_wool 1

execute if score @s cf_block_wool matches 2 run scoreboard players set @s cf_block_wool 0

function color_field:render/blocks/set
