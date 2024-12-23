input_txt = open('day17.txt', mode='r')
lines = input_txt.readlines()

A = int(lines[0].split(":")[1])
B = int(lines[1].split(":")[1])
C = int(lines[2].split(":")[1])
IP = 0

OUTPUT = []
PROGRAM = [int(x) for x in lines[4].split(":")[1].strip().split(",")]

def combo_op(operand):
    global A, B, C
    if operand > 3:
        operand = [A, B, C][operand-4]
    return operand

def adv(operand):
    global A
    operand = combo_op(operand)
    A = A // 2**operand
def bxl(operand):
    global B
    B = B ^ operand
def bst(operand):
    global B
    operand = combo_op(operand)
    B = operand % 8
def jnz(operand):
    global A, IP
    if A:
        IP = operand
def bxc(operand):
    global B, C
    B = B ^ C
def out(operand):
    operand = combo_op(operand)
    OUTPUT.append(operand % 8)
def bdv(operand):
    global A, B
    operand = combo_op(operand)
    B = A // 2**operand
def cdv(operand):
    global A, C
    operand = combo_op(operand)
    C = A // 2**operand

op_table = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}

# Part 1
while IP < len(PROGRAM):
    operand = PROGRAM[IP+1]
    func = op_table[PROGRAM[IP]]
    func(operand)
    IP += 2 if func != jnz or not A else 0
print(",".join(map(str, OUTPUT)))