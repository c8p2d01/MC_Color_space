# toggle on

execute if score @s cf_block_end matches 1 run scoreboard players set @s cf_block_end 2

execute unless score @s cf_block_end matches 1..2 run scoreboard players set @s cf_block_end 1

execute if score @s cf_block_end matches 2 run scoreboard players set @s cf_block_end 0

function color_field:render/blocks/set
