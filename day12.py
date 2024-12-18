from collections import Counter

input_txt = open('day12.txt', mode='r')
lines = input_txt.readlines()
map = [[c for c in line.strip()] for line in lines]

# Part 1
found = []

def get_unfound_neighbors(x, y, search):
    res = []
    if 0 <= y-1 and map[y-1][x] == search and (x, y-1) not in found:
        res.append((x, y-1))
    if y+1 < len(map) and map[y+1][x] == search and (x, y+1) not in found:
        res.append((x, y+1))
    if 0 <= x-1 and map[y][x-1] == search and (x-1, y) not in found:
        res.append((x-1, y))
    if x+1 < len(map[y]) and map[y][x+1] == search and (x+1, y) not in found:
        res.append((x+1, y))
    return res

def count_neighbors(x, y, search):
    res = 0
    if 0 <= y-1 and map[y-1][x] == search:
        res += 1
    if y+1 < len(map) and map[y+1][x] == search:
        res += 1
    if 0 <= x-1 and map[y][x-1] == search:
        res += 1
    if x+1 < len(map[y]) and map[y][x+1] == search:
        res += 1
    return res

def DFS_cost(x, y, search):
    if (x, y) in found:
        return 0, 0
    found.append((x, y))
    unfound_neighbors = get_unfound_neighbors(x, y, search)
    area, perimeter = (1, 4-count_neighbors(x, y, search))
    for unfound_neighbor in unfound_neighbors:
        cost_area, cost_perim = DFS_cost(*unfound_neighbor, search)
        area += cost_area
        perimeter += cost_perim
    return area, perimeter

total_costs = 0
for y in range(len(map)):
    for x in range(len(map[y])):
        cost = DFS_cost(x, y, map[y][x])
        total_costs += cost[0]*cost[1]

print(total_costs)

# Part 2