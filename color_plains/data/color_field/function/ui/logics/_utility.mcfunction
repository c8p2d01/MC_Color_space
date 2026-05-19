# toggle on

execute if score @s cf_block_utility matches 1 run scoreboard players set @s cf_block_utility 2

execute unless score @s cf_block_utility matches 1..2 run scoreboard players set @s cf_block_utility 1

execute if score @s cf_block_utility matches 2 run scoreboard players set @s cf_block_utility 0

function color_field:render/blocks/set
