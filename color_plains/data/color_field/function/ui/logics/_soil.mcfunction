# toggle on

execute if score @s cf_block_soil matches 1 run scoreboard players set @s cf_block_soil 2

execute unless score @s cf_block_soil matches 1..2 run scoreboard players set @s cf_block_soil 1

execute if score @s cf_block_soil matches 2 run scoreboard players set @s cf_block_soil 0

function color_field:render/blocks/set
