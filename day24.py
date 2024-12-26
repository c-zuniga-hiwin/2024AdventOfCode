import re

input_txt = open('day24.txt', mode='r')
lines = input_txt.readlines()

data = {}
computations = []

for line in lines:
    line = line.strip()
    if not line:
        continue
    start_info = line.split(":")
    comp_info = line.split("->")
    if len(start_info) > 1:
        data[start_info[0]] = bool(int(start_info[1].strip()))
    else:
        comp = {
            "Operands": [comp_info[0].split(" ")[0], comp_info[0].split(" ")[2]],
            "Operation": comp_info[0].split(" ")[1].replace("AND", "&").replace("XOR", "^").replace("OR", "|"),
            "Result": comp_info[1].strip()
        }
        comp["DependenciesLeft"] = list(filter(lambda x: x not in data.keys(), comp["Operands"]))
        computations.append(comp)

while computations:
    computations = sorted(computations, key=lambda x: len(x["DependenciesLeft"]))
    computation = computations[0]
    data[computation["Result"]] = eval(f"{data[computation["Operands"][0]]} {computation["Operation"]} {data[computation["Operands"][1]]}")
    for comp in computations[1:]:
        comp["DependenciesLeft"] = list(filter(lambda x: x not in data.keys(), comp["Operands"]))
    del computations[0]

z_vals = {k: v for k, v in sorted(data.items(), reverse=True) if re.search(r"^z\d*$", k)}
binary_string = ''.join(['1' if x else '0' for x in z_vals.values()])
res = int(binary_string, 2)
print(res)