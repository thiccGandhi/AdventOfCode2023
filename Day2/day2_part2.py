import math

file = open("day2_input.txt", "r")
cum_sum = 0

for line in file:
    game_id, game_data = line.split(":")
    game_data = game_data.split(";")
    min_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for ind_set in game_data:
        ind_data = ind_set.split(",")
        for x in ind_data:
            a = x.strip().split(" ")
            if int(a[0]) > min_cubes[a[1]]:
                min_cubes.update({a[1]: int(a[0])})
    game_product = math.prod(min_cubes.values())
    cum_sum += game_product
print(cum_sum)
