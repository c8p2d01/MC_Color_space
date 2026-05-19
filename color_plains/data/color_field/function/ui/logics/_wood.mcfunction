# toggle on

execute if score @s cf_block_wood matches 1 run scoreboard players set @s cf_block_wood 2

execute unless score @s cf_block_wood matches 1..2 run scoreboard players set @s cf_block_wood 1

execute if score @s cf_block_wood matches 2 run scoreboard players set @s cf_block_wood 0

function color_field:render/blocks/set
