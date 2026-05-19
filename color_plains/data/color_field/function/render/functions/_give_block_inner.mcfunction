
# better version (dynamic, requires storage)
data modify storage color_field:block set from entity @s block_state.Name
execute store result score #tmp dummy run data get storage color_field:block
