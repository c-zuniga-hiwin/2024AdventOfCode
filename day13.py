input_txt = open('day13.txt', mode='r')
lines = input_txt.readlines()

games = []

curr_game = {}
for line in lines:
    line = line.strip()
    if not line:
        games.append(curr_game)
        curr_game = {}
        continue
    game_details = line.split(":")
    # Buttons
    if game_details[1].count("+"):
        curr_game[game_details[0].split(" ")[-1]] = {
            "X": int(game_details[1].split(",")[0][3:]),
            "Y": int(game_details[1].split(",")[1][3:])
        }
    # Prizes
    else:
        curr_game[game_details[0]] = {
            "X": int(game_details[1].split(",")[0][3:]),
            "Y": int(game_details[1].split(",")[1][3:])
        }
games.append(curr_game)

# Part 1
def min_cost(x, y, game_info):
    if (x, y) in memo_cost:
        return memo_cost.get((x, y))
    if x < 0 or y < 0:
        return float('inf')
    if x == 0 and y == 0:
        return 0
    
    cost_a = min_cost(x-game["A"]["X"], y-game["A"]["Y"], game_info)
    cost_b = min_cost(x-game["B"]["X"], y-game["B"]["Y"], game_info)
    min_cost_res = min(3+cost_a, 1+cost_b)
    memo_cost[(x, y)] = min_cost_res
    return min_cost_res

res = 0
for game in games:
    memo_cost = {}
    game_cost = min_cost(game["Prize"]["X"],game["Prize"]["Y"], game)
    res += game_cost if game_cost != float('inf') else 0
print(res)

# Part 2
import numpy as np

res = 0
for game in games:
    game["Prize"]["X"] += 10000000000000
    game["Prize"]["Y"] += 10000000000000
    x_y = np.array([[game["A"]["X"], game["B"]["X"]], [game["A"]["Y"], game["B"]["Y"]]])
    prize = np.array([game["Prize"]["X"], game["Prize"]["Y"]])
    x = np.linalg.solve(x_y, prize)
    num_a, num_b = round(x[0]), round(x[1])
    if num_a*game["A"]["X"]+num_b*game["B"]["X"] == game["Prize"]["X"] and num_a*game["A"]["Y"]+num_b*game["B"]["Y"] == game["Prize"]["Y"]:
        res += num_a*3 + num_b

print(res)