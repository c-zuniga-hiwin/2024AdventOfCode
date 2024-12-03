import re

input_txt = open('day3.txt', mode='r')
lines = input_txt.readlines()

# Part 1
total = 0
for line in lines:
    matches = re.findall(r"mul\([0-9]+,[0-9]+\)", line)
    mults = [match[4:-1] for match in matches]
    total += sum([int(mult.split(",")[0])*int(mult.split(",")[1]) for mult in mults])
print(total)

# Part 2
total = 0
enable_mult = True
for line in lines:
    matches = re.findall(r"mul\([0-9]+,[0-9]+\)|don't\(\)|do\(\)", line)
    for match in matches:
        if match == "do()":
            enable_mult = True
        elif match == "don't()":
            enable_mult = False
        elif enable_mult:
            total += int(match[4:-1].split(",")[0])*int(match[4:-1].split(",")[1])
print(total)