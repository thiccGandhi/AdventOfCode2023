file = open("day1_input.txt", "r")
cum_sum = 0
for line in file:
    nums = [i for i in line if i.isdigit()]
    line_value = int(nums[0] + nums[-1])
    cum_sum += line_value
print(cum_sum)
