from re import split


input_txt = open('day6.txt', mode='r')
lines = input_txt.readlines()
map = [list(line.split()[0]) for line in lines]

GUARD_CHAR = "^"
VISITED_CHAR = "X"
OBSTACLE_CHAR = "#"

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == GUARD_CHAR:
            guard_pos = (i, j)
            break

# Part 1

# looking up, so i decreases, j does not change
direction = (-1, 0)

def get_next_pos():
    return tuple(a + b for a, b in zip(guard_pos, direction))
def within_bounds(pos):
    return 0 <= pos[0] < len(map) and 0 <= pos[1] < len(map[0])
def rotate_90():
    new_y = 0 if direction[0] else 1 if direction[1] == 1 else -1
    new_x = 0 if direction[1] else 1 if direction[0] == -1 else -1
    return (new_y, new_x)

while within_bounds(guard_pos):
    map[guard_pos[0]][guard_pos[1]] = VISITED_CHAR
    next_pos = get_next_pos()
    if not within_bounds(next_pos):
        guard_pos = get_next_pos()
        continue
    if map[next_pos[0]][next_pos[1]] == OBSTACLE_CHAR:
        direction = rotate_90()
    guard_pos = get_next_pos()
print(sum([x.count(VISITED_CHAR) for x in map]))

# Part 2
def looping(new_map, starting_guard_pos):
    guard_pos_new = tuple(starting_guard_pos)
    visited = []
    direction_new = (-1, 0)
    def get_next_pos():
        return tuple(a + b for a, b in zip(guard_pos_new, direction_new))
    def within_bounds(pos):
        return 0 <= pos[0] < len(new_map) and 0 <= pos[1] < len(new_map[0])
    def rotate_90():
        new_y = 0 if direction_new[0] else 1 if direction_new[1] == 1 else -1
        new_x = 0 if direction_new[1] else 1 if direction_new[0] == -1 else -1
        return (new_y, new_x)
    
    while within_bounds(guard_pos_new):
        if visited.count(get_next_pos()):
            return True
        visited.append(guard_pos_new)
        # print("Visited", visited)
        next_pos = get_next_pos()
        if not within_bounds(next_pos):
            guard_pos_new = get_next_pos()
            continue
        if new_map[next_pos[0]][next_pos[1]] == OBSTACLE_CHAR:
            direction_new = rotate_90()
        guard_pos_new = get_next_pos()
    return False

result = 0
map = [list(line.split()[0]) for line in lines]
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == GUARD_CHAR:
            starting_guard_pos = (i, j)
            break
for i in range(len(map)):
    for j in range(len(map[i])):
        print(i, j)
        if (i, j) == starting_guard_pos:
            continue
        map[i][j] = OBSTACLE_CHAR
        if looping(map, starting_guard_pos):
            result += 1
        map = [list(line.split()[0]) for line in lines]
print(result)