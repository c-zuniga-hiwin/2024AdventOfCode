input_txt = open('day11.txt', mode='r')
lines = input_txt.readlines()
line = lines[0].strip().split()

def blink(nums):
    res = []
    for num in nums:
        if num == '0':
            res.append('1')
        elif len(num) % 2 == 0:
            res.append(str(int(num[:len(num)//2])))
            res.append(str(int(num[len(num)//2:])))
        else:
            res.append(str(int(num)*2024))
    return res
    
result = line[:]
for i in range(25):
    result = blink(result)

print(len(result))

# Part 2
from collections import Counter
line = [int(char) for char in lines[0].strip().split()]
def blink(nums):
    res = {}
    for key, val in nums.items():
        str_num = str(key)
        if not key:
            res[1] = res.get(1, 0)+val
        elif len(str_num) % 2 == 0:
            left = int(str_num[:len(str_num)//2])
            right = int(str_num[len(str_num)//2:])
            res[left] = res.get(left, 0)+val
            res[right] = res.get(right, 0)+val
        else:
            mult_num = key*2024
            res[mult_num] = res.get(mult_num, 0)+val
    return res

result = Counter(line)
for i in range(75):
    result = blink(result)

print(sum(result.values()))