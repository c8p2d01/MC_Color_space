# toggle on

execute if score @s cf_block_dirt matches 1 run scoreboard players set @s cf_block_dirt 2

execute unless score @s cf_block_dirt matches 1..2 run scoreboard players set @s cf_block_dirt 1

execute if score @s cf_block_dirt matches 2 run scoreboard players set @s cf_block_dirt 0

function color_field:render/blocks/set
