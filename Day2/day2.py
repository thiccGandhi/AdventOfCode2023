file = open("day2_input.txt", "r")
possible = {
    "red": 12,
    "green": 13,
    "blue": 14
}
cum_sum = 0

for line in file:
    is_possible = True
    game_id, game_data = line.split(":")
    game_id = game_id.split(" ")[1]
    game_data = game_data.split(";")

    for ind_set in game_data:
        ind_data = ind_set.split(",")
        for x in ind_data:
            a = x.strip().split(" ")
            if int(a[0]) > possible[a[1]]:
                is_possible = False
    if is_possible:
        cum_sum += int(game_id)
print(cum_sum)

