# toggle on

execute if score @s cf_block_stone matches 1 run scoreboard players set @s cf_block_stone 2

execute unless score @s cf_block_stone matches 1..2 run scoreboard players set @s cf_block_stone 1

execute if score @s cf_block_stone matches 2 run scoreboard players set @s cf_block_stone 0

function color_field:render/blocks/set
