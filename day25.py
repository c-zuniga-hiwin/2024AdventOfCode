import re
import numpy as np

input_txt = open('day25.txt', mode='r')
lines = input_txt.readlines()

keys = []
locks = []

curr_body = []
for line in lines+["\n"]:
    line = line.strip()

    if line:
        curr_body.append(line)

    else:
        if re.match(r"^\.+$", curr_body[0]):
            keys.append(np.array([list(x) for x in curr_body]))
        else:
            locks.append(np.array([list(x) for x in curr_body]))
        curr_body = []

keys = [np.sum(key[:-1] == '#', axis=0) for key in keys]
locks = [np.sum(lock[1:] == '#', axis=0) for lock in locks]

res = 0
check_arr = np.array([5]*5)
for key in keys:
    for lock in locks:
        if np.all(key+lock <= 5):
            res += 1
print(res)