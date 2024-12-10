from re import split


input_txt = open('day5.txt', mode='r')
lines = input_txt.readlines()

depends_on = {}
good_lines = []
for line in lines:
    if not line.split():
        continue
    line = line.strip()
    splitted = line.split("|")
    if len(splitted) == 2:
        depends_on[splitted[1]] = depends_on.get(splitted[1], []) + [splitted[0]]
        continue
    splitted = line.split(",")
    good_line = True
    for i, page in enumerate(splitted):
        print(page, splitted, depends_on.get(page))
        if not all([x not in depends_on.get(page, []) for x in splitted[i+1:]]):
            good_line = False
            break
    if good_line:
        good_lines.append(splitted)
print(sum([int(line[len(line)//2]) for line in good_lines]))

# Part 2. Start from the right
def correct_line(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[j] in depends_on.get(arr[i], []):
                ...

result = []
for line in lines:
    if not line.split():
        continue
    line = line.strip()
    splitted = line.split(",")
    good_line = True
    for i, page in enumerate(splitted):
        if not all([x not in depends_on.get(page, []) for x in splitted[i+1:]]):
            result.append(correct_line(splitted))
            break
print(result)
print(sum([int(line[len(line)//2]) for line in result]))