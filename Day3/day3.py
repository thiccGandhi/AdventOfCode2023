file = open("day3_input.txt", "r")
nums = []
symbols = []
cum_sum = 0

for line_num, line in enumerate(file):
    for x_num, x in enumerate(line):
        if x.isdigit():
            nums.append([str(line_num), str(x_num), x])
        elif x != "." and x != "\n":
            symbols.append([str(line_num), str(x_num), x])

counter = 1
while counter < len(nums):
    if nums[counter][0] == nums[counter-1][0] and int(nums[counter][1]) == int(nums[counter-1][1]) + 1:
        nums[counter-1] = [nums[counter-1][0], nums[counter][1], nums[counter-1][2] + nums[counter][2]]
        nums.pop(counter)
    else:
        counter += 1

for x in nums:
    x_min = int(x[1]) - len(x[2])
    x_max = int(x[1]) + 1
    y_min = int(x[0]) - 1
    y_max = int(x[0]) + 1
    for s in symbols:
        if x_min <= int(s[1]) <= x_max and y_min <= int(s[0]) <= y_max:
            cum_sum += int(x[2])
            break

print(cum_sum)
