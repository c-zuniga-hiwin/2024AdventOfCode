import numpy as np
from heapq import heapify, heappush, heappop 

input_txt = open('day16.txt', mode='r')
lines = input_txt.readlines()

maze = [[c for c in line.strip()] for line in lines]
maze = np.array(maze)

OBSTACLE_CHAR = "#"
EMPTY_CHAR = "."
START_CHAR = "S"
END_CHAR = "E"
TURN_COST = 1000

# y, x
start_pos = np.array([len(maze)-2, 1])
end_pos = np.array([1, len(maze[0])-2])
direction = np.array([0, 1])

def rotate_direction(direction, wise):
    # 0,1 -> -1,0   0,-1 -> 1,0     1,0 -> 0,1      -1,0 -> 0,-1
    if wise == "CCW":
        rotation_matrix = np.array([[0, 1],
                             [-1, 0]])
        return direction @ rotation_matrix
    elif wise == "CW":
        rotation_matrix = np.array([[0, -1],
                             [1,  0]])
        return direction @ rotation_matrix

def distance(pos):
    return np.sum(np.abs(end_pos-pos))

# Returns [(heuristic cost, actual cost, position, direction)]
def get_neighbors(pos, direction):
    res = []
    ccw_direction = rotate_direction(direction, "CCW")
    cw_direction = rotate_direction(direction, "CW")
    ccw_pos = pos + ccw_direction
    cw_pos = pos + cw_direction
    next_pos = pos + direction
    # Use Manhattan distance to end as heuristic for cost
    if 0 <= ccw_pos[0] < len(maze) and 0 <= ccw_pos[1] < len(maze[0]) and maze[tuple(ccw_pos)] != START_CHAR and maze[tuple(ccw_pos)] != OBSTACLE_CHAR:
        res.append((TURN_COST+distance(ccw_pos), TURN_COST+1, tuple(ccw_pos), tuple(ccw_direction)))
    if 0 <= cw_pos[0] < len(maze) and 0 <= cw_pos[1] < len(maze[0]) and maze[tuple(cw_pos)] != START_CHAR and maze[tuple(cw_pos)] != OBSTACLE_CHAR:
        res.append((TURN_COST+distance(cw_pos), TURN_COST+1, tuple(cw_pos), tuple(cw_direction)))
    if 0 <= next_pos[0] < len(maze) and 0 <= next_pos[1] < len(maze[0]) and maze[tuple(next_pos)] != START_CHAR and maze[tuple(next_pos)] != OBSTACLE_CHAR:
        res.append((distance(next_pos), 1, tuple(next_pos), tuple(direction)))
    return res

# Part 1
visited = set()
heap = [(distance(start_pos), 0, tuple(start_pos), tuple(direction))]
heapify(heap)
while heap:
    heuristic_cost, actual_cost, pos, direction = heappop(heap)
    if pos == tuple(end_pos):
        print(actual_cost)
        break
    if (pos, direction) in visited:
        continue
    visited.add((pos, direction))
    neighbors = get_neighbors(np.array(pos), np.array(direction))
    for neighbor in neighbors:
        neighbor_heuristic_cost, neighbor_actual_cost, neighbor_pos, neighbor_direction = neighbor
        heappush(heap, (neighbor_heuristic_cost+actual_cost, neighbor_actual_cost+actual_cost, neighbor_pos, neighbor_direction))

# Part 2