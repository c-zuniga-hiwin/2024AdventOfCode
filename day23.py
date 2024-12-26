input_txt = open('day23.txt', mode='r')
lines = input_txt.readlines()

edges = {}

for line in lines:
    line = line.strip()
    data = line.split("-")
    edges[data[0]] = edges.get(data[0], []) + [data[1]]
    edges[data[1]] = edges.get(data[1], []) + [data[0]]

# Part 1
groups = []

for node, neighbors in edges.items():
    for neighbor in neighbors:
        # to avoid duplicates
        if neighbor > node:
            common_neighbors = set(neighbors).intersection(edges[neighbor])
            for common_neighbor in common_neighbors:
                # to avoid duplicates
                if common_neighbor > neighbor:
                    groups.append([node, neighbor, common_neighbor])

start_with_t = list(filter(lambda x: any([computer[0] == 't' for computer in x]), groups))
print(len(start_with_t))

# Part 2
groups = []
visited = set()

for node, neighbors in edges.items():
    if node not in visited:
        group = [node]
        visited.add(node)

        for neighbor in neighbors:
            if all(neighbor in edges[member] for member in group):
                group.append(neighbor)
                visited.add(neighbor)
        if len(group) > 1:
            groups.append(group)

max_group = max(groups, key=lambda x: len(x))
print(','.join(sorted(max_group)))