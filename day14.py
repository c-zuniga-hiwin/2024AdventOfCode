input_txt = open('day14.txt', mode='r')
lines = input_txt.readlines()

WIDTH = 101
HEIGHT = 103
NUM_SECONDS = 100

robots = []

for line in lines:
    if not line:
        break
    line = line.strip()
    x_y = line.split(" ")[0]
    vel = line.split(" ")[1]
    robots.append({
        "X": int(x_y.split(",")[0][2:]),
        "Y": int(x_y.split(",")[1]),
        "v_x": int(vel.split(",")[0][2:]),
        "v_y": int(vel.split(",")[1]),
    })

# Part 1
end_robots = []
for robot in robots:
    end_pos = ((robot["X"]+robot["v_x"]*NUM_SECONDS) % WIDTH, (robot["Y"]+robot["v_y"]*NUM_SECONDS) % HEIGHT)
    end_robots.append(end_pos)

top_left = list(filter(lambda pos: pos[0] < WIDTH//2 and pos[1] < HEIGHT//2, end_robots))
top_right = list(filter(lambda pos: pos[0] > WIDTH//2 and pos[1] < HEIGHT//2, end_robots))
bottom_left = list(filter(lambda pos: pos[0] < WIDTH//2 and pos[1] > HEIGHT//2, end_robots))
bottom_right = list(filter(lambda pos: pos[0] > WIDTH//2 and pos[1] > HEIGHT//2, end_robots))
quads = [top_left, top_right, bottom_left, bottom_right]

res = 1
for quad in quads:
    res *= max(len(quad), 1)
print(res)

# Part 2
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import clear_output
import time

# plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.figure(figsize=(10, 6))
plt.rcParams["figure.autolayout"] = True
plt.xlim(WIDTH)
plt.ylim(HEIGHT)
map = [[0 for _ in range(WIDTH)] for __ in range(HEIGHT)]

def show_map(map):
    x = []
    y = []
    
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] != 0:  # Non-zero values
                x.append(j)  # j corresponds to WIDTH (x-axis)
                y.append(i)  # i corresponds to HEIGHT (y-axis)

    # Plot the scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, cmap='viridis', alpha=0.8, edgecolors='k')
    plt.title('2D Array Map Visualization')
    plt.xlabel(f"Time: {num_secs}")
    plt.ylabel('Height (Y-axis)')
    plt.xlim(0, WIDTH)
    plt.ylim(0, HEIGHT)
    plt.gca().invert_yaxis()  # Invert y-axis to match array indexing
    plt.colorbar(label='Values')
    plt.grid(True)
    plt.show()

TOO_LOW = 4019
# skip first TOO_LOW iterations, im cheesing it lol
for robot in robots:
    end_pos = ((robot["X"]+robot["v_x"]*TOO_LOW) % WIDTH, (robot["Y"]+robot["v_y"]*TOO_LOW) % HEIGHT)
    robot["X"], robot["Y"] = end_pos[0], end_pos[1]

num_secs = TOO_LOW
while True:
    map = [[0 for _ in range(WIDTH)] for __ in range(HEIGHT)]
    for robot in robots:
        end_pos = ((robot["X"]+robot["v_x"]) % WIDTH, (robot["Y"]+robot["v_y"]) % HEIGHT)
        robot["X"], robot["Y"] = end_pos[0], end_pos[1]
        map[robot["Y"]][robot["X"]] = 1
    data = np.array(map)
    show_map(data)
    num_secs += 1    
    # time.sleep(0.01)
    clear_output(wait=True)