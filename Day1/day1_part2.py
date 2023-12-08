file = open("day1_input.txt", "r")
cum_sum = 0
number_words = {
    "one": "o1e",
    "two": "t2o",
    "three": "thr3e",
    "four": "f4ur",
    "five": "f5ve",
    "six": "s6x",
    "seven": "se7en",
    "eight": "ei8ht",
    "nine": "n9ne",
}
window_size = 5


def check_for_replace(line_to_replace):
    for word in number_words.keys():
        line_to_replace = line_to_replace.replace(word, number_words[word], 1)
    return line_to_replace


def check_word(word_to_check):
    for i in range(len(word_to_check) - window_size + 1):
        x = check_for_replace(word_to_check[i:i + window_size])
        if x != word_to_check[i:i + window_size]:
            word_to_check = word_to_check.replace(word_to_check[i:i+window_size], x)
    return word_to_check


for line in file:
    line = check_word(line)
    nums = [i for i in line if i.isdigit()]
    line_value = int(nums[0] + nums[-1])
    cum_sum += line_value
print(cum_sum)
