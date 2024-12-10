input_txt = open('day7.txt', mode='r')
lines = input_txt.readlines()

forms = {}
for line in lines:
    forms[int(line.split(":")[0])] = [int(x) for x in line.split(":")[1].split()]

# Part 1
def calc_line_items(arr):
    if not len(arr):
        return 0
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return [arr[0]*arr[1], arr[0]+arr[1]]
    results = calc_line_items(arr[:-1])
    return [arr[-1]+res for res in results] + [arr[-1]*res for res in results]

result = 0
for key, val in forms.items():
    res = calc_line_items(val)
    if key in res:
        result += key
print(result)

# Part 2
def calc_line_items(arr):
    if not len(arr):
        return 0
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return [arr[0]*arr[1], arr[0]+arr[1], int(str(arr[0]) + str(arr[1]))]
    results = calc_line_items(arr[:-1])
    return [arr[-1]+res for res in results] + [arr[-1]*res for res in results] + [int(str(res) + str(arr[-1])) for res in results]

result = 0
for key, val in forms.items():
    res = calc_line_items(val)
    if key in res:
        result += key
print(result)