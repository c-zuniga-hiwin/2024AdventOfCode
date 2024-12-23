input_txt = open('day22.txt', mode='r')
lines = input_txt.readlines()
secret_nums = [int(line) for line in lines]

# Notes: multiplying by 64 is same as bit shift left 6, dividing by 32 is just shift right 5, multiplying by 2048 is just bit shift 11
# Mixing is just xor
# Modulo 16777216 is same as taking the lower 24 bits, IE AND 16,777,215
def hash(secret_num):
    secret_num = ((secret_num << 6) ^ secret_num) & 16_777_215
    secret_num = ((secret_num >> 5) ^ secret_num) & 16_777_215
    secret_num = ((secret_num << 11) ^ secret_num) & 16_777_215
    return secret_num

res = []
for secret_num in secret_nums:
    for _ in range(2000):
        secret_num = hash(secret_num)
    res.append(secret_num)
print(sum(res))