input_txt = open('day4.txt', mode='r')
lines = input_txt.readlines()

# Part 1

def check_square(i, j):
    count = 0
    # check right
    if j + 4 <= len(lines[i]):
        count += 1 if all(lines[i][j + k] == "XMAS"[k] for k in range(4)) else 0
    # check left
    if j - 3 >= 0:
        count += 1 if all(lines[i][j - k] == "XMAS"[k] for k in range(4)) else 0
    # check down
    if i + 4 <= len(lines):
        count += 1 if all(lines[i + k][j] == "XMAS"[k] for k in range(4)) else 0
    # check up
    if i - 3 >= 0:
        count += 1 if all(lines[i - k][j] == "XMAS"[k] for k in range(4)) else 0
    # check down and to the right
    if i + 4 <= len(lines) and j + 4 <= len(lines[i]):
        count += 1 if all(lines[i + k][j + k] == "XMAS"[k] for k in range(4)) else 0
    # check down and to the left
    if i + 4 <= len(lines) and j - 3 >= 0:
        count += 1 if all(lines[i + k][j - k] == "XMAS"[k] for k in range(4)) else 0
    # check up and to the right
    if i - 3 >= 0 and j + 4 <= len(lines[i]):
        count += 1 if all(lines[i - k][j + k] == "XMAS"[k] for k in range(4)) else 0
    # check up and to the left
    if i - 3 >= 0 and j - 3 >= 0:
        count += 1 if all(lines[i - k][j - k] == "XMAS"[k] for k in range(4)) else 0
    return count
res = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        res += check_square(i, j)
print(res)

# Part 2
def check_square_a(i, j):
    if i > 0 and i + 1 < len(lines) and j > 0 and j + 1 < len(lines[i]):
        # check top left and bottom right, then top right and bottom left
        if sorted([lines[i-1][j-1], lines[i+1][j+1]]) == ["M", "S"] and sorted([lines[i-1][j+1], lines[i+1][j-1]]) == ["M", "S"]:
            return True
    return False

res = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "A" and check_square_a(i, j):
            res += 1
print(res)