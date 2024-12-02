input_txt = open('day1.txt', mode='r')
lines = input_txt.readlines()

# Part 1
pairs = [line.split() for line in lines]
left = [int(pair[0]) for pair in pairs]
right = [int(pair[1]) for pair in pairs]

left.sort()
right.sort()

print(sum([abs(left[i] - right[i])for i in range(len(left))]))

# Part 2
print(sum([num*right.count(num) for num in left]))