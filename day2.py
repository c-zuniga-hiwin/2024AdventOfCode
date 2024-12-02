input_txt = open('day2.txt', mode='r')
lines = input_txt.readlines()

levels = [line.split() for line in lines]

# Part 1
def check_safe(level):
    level = [int(x) for x in level]
    if level != sorted(level) and level != sorted(level, reverse=True):
        return False
    last = level[0]
    for num in level[1:]:
        if abs(num-last) < 1 or abs(num-last) > 3:
            return False
        last = num
    return True

result = 0
for level in levels:
    if check_safe(level):
        result += 1

print(result)

# Part 2
# Algorithm (very slow): remove each number one-by-one and check if safe
result = 0
for level in levels:
    for i in range(len(level)):
        if check_safe(level[:i]+level[i+1:]):
            result += 1
            break
print(result)