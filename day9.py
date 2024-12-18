input_txt = open('day9.txt', mode='r')
lines = input_txt.readlines()
line = [int(x) for x in lines[0].strip()]

# Part 1
id_count = {}
empty_spaces = {}
for i in range(0, len(line), 2):
    id_count[i//2] = line[i]
    empty_spaces[i//2] = line[i+1] if i+1 < len(line) else 0

data = []
for key in id_count.keys():
    data += [key]*id_count[key]
    id_count[key] = 0
    for x in reversed(id_count.keys()):
        if id_count[x] == 0:
            continue
        elif empty_spaces[key] <= id_count[x]:
            data += [x]*empty_spaces[key]
            id_count[x] -= empty_spaces[key]
            empty_spaces[key] = 0
            break
        elif empty_spaces[key] > id_count[x]:
            data += [x]*id_count[x]
            empty_spaces[key] -= id_count[x]
            id_count[x] = 0

print(sum([data[i]*i for i in range(len(data))]))

# Part 2
# index of last occurance
def rindex(arr, elem):
    return len(arr) - 1 - list(reversed(arr)).index(elem)

id_count = {}
empty_spaces = {}
for i in range(0, len(line), 2):
    id_count[i//2] = line[i]
    empty_spaces[i//2] = line[i+1] if i+1 < len(line) else 0

order = list(id_count.keys())
for key in reversed(id_count.keys()):
    for key_e in empty_spaces.keys():
        if empty_spaces[key_e] >= id_count[key]:
            order.remove(key_e)
            order = order[:]