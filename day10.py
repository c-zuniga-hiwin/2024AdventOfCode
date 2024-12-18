input_txt = open('day10.txt', mode='r')
lines = input_txt.readlines()
map = [[int(char) for char in line.strip()] for line in lines]

# Part 1
seen_starts = {}
def get_score(x, y, num, start_x, start_y):
    if not 0 <= x < len(map[0]) or not 0 <= y < len(map):
        return 0
    if num == 0 and map[y][x] == 0:
        if f"{x}, {y}" not in seen_starts.get(f"{start_x}, {start_y}", []):
            seen_starts[f"{start_x}, {start_y}"] = seen_starts.get(f"{start_x}, {start_y}", []) + [f"{x}, {y}"]
            return 1
    if map[y][x] != num:
        return 0
    return get_score(x-1,y,num-1, start_x, start_y)+get_score(x,y-1,num-1, start_x, start_y)+get_score(x+1,y,num-1, start_x, start_y)+get_score(x,y+1,num-1, start_x, start_y)

result = 0
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == 9:
            result += get_score(x, y, 9, x, y)
print(result)

# Part 2
def get_score(x, y, num):
    if not 0 <= x < len(map[0]) or not 0 <= y < len(map):
        return 0
    if num == 0 and map[y][x] == 0:
            return 1
    if map[y][x] != num:
        return 0
    return get_score(x-1,y,num-1)+get_score(x,y-1,num-1)+get_score(x+1,y,num-1)+get_score(x,y+1,num-1)

result = 0
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == 9:
            result += get_score(x, y, 9)
print(result)