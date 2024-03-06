import os, sys, random
# Initialization
markers = {transVars(program[x][1:]):x for x in range(len(program)) if program[x].startswith(':')}
memory = {}
pointer = 0
i = 0
# Functions
def error(s):
    input(str(i)+': '+s)
    sys.exit()
def number(n):
    return None if n == 'nil' else (float(n) if ('.' in str(n)) else int(n))
def transVars(s):
    while '@' in s:
        for cell in memory: s = s.replace('@'+str(cell), str(memory[cell]))
    return number(s)
# Open program
if not len(sys.argv) > 1: sys.exit()
if not os.path.exists(sys.argv[1]): error("File not found: %s"%sys.argv[1])
with open(sys.argv[1], 'r') as f:
    program = [token.strip() for token in f.read().split()]
# Imports
for token in range(len(program)):
    if program[token].startswith('!'):
        path = program[token][1:]
        if os.path.exists(path):
            with open(path, 'r') as f:
                program.pop(token)
                program[token:token] = [i.strip() for i in f.read().split()]
while i < len(program):
    instruction = program[i]
    # Pointer
    if instruction == '>': pointer += 1
    elif instruction == '<': pointer -= 1
    elif instruction == '>>':
        pointer += transVars(program[i+1])
        i += 1
    elif instruction == '<<':
        pointer -= transVars(program[i+1])
        i += 1
    elif instruction == '~':
        pointer = transVars(program[i+1])
        i += 1
    # Arithmetic
    elif instruction == '++': memory[pointer] += 1
    elif instruction == '--': memory[pointer] -= 1
    elif instruction == '+':
        memory[pointer] += transVars(program[i+1])
        i += 1
    elif instruction == '-':
        memory[pointer] -= transVars(program[i+1])
        i += 1
    elif instruction == '*':
        memory[pointer] *= transVars(program[i+1])
        i += 1
    elif instruction == '/':
        try: memory[pointer] /= transVars(program[i+1])
        except ZeroDivisionError: error("Cannot divide by zero")
        i += 1
    elif instruction == '//':
        try: memory[pointer] //= transVars(program[i+1])
        except ZeroDivisionError: error("Cannot divide by zero")
        i += 1
    elif instruction == '^':
        memory[pointer] **= transVars(program[i+1])
        i += 1
    elif instruction == '%':
        try: memory[pointer] %= transVars(program[i+1])
        except ZeroDivisionError: error("Cannot mod by zero")
        i += 1
    elif instruction == '\\':
        memory[pointer] = memory[pointer]**(1/transVars(program[i+1]))
        i += 1
    elif instruction == 'round':
        memory[pointer] = round(memory[pointer])
    elif instruction == 'ceil':
        memory[pointer] = math.ceil(memory[pointer])
    elif instruction == 'floor':
        memory[pointer] = math.floor(memory[pointer])
    elif instruction == 'sin':
        memory[pointer] = math.sin(memory[pointer])
    elif instruction == 'cos':
        memory[pointer] = math.cos(memory[pointer])
    elif instruction == 'tan':
        memory[pointer] = math.tan(memory[pointer])
    elif instruction == 'log':
        if transVars(program[i+1]) > 1: memory[pointer] = math.log(memory[pointer], transVars(program[i+1]))
        else: error("Log base must be 2 or greater")
        i += 1
    elif instruction == 'fact':
        try: memory[pointer] = math.factorial(transVars(program[i+1]))
        except: error("Cannot convert %s to number"%program[i+1])
        i += 1
    elif instruction == 'abs': memory[pointer] = abs(memory[pointer])
    elif instruction == 'rand':
        try: memory[pointer] = random.randint(transVars(program[i+1]), transVars(program[i+2]))
        except:
            try:
                transVars(program[i+1])
                error("Cannot convert %s to number"%program[i+2])
            except: error("Cannot convert %s to number"%program[i+1])
        i += 2
    # Logic
    elif instruction == 'eq':
        memory[pointer] = int(memory[pointer]==transVars(program[i+1]))
        i += 1
    elif instruction == 'gt':
        memory[pointer] = int(memory[pointer]>transVars(program[i+1]))
        i += 1
    elif instruction == 'gte':
        memory[pointer] = int(memory[pointer]>=transVars(program[i+1]))
        i += 1
    elif instruction == 'lt':
        memory[pointer] = int(memory[pointer]<transVars(program[i+1]))
        i += 1
    elif instruction == 'lte':
        memory[pointer] = int(memory[pointer]<=transVars(program[i+1]))
        i += 1
    elif instruction == 'not': memory[pointer] = int(not memory[pointer])
    elif instruction == 'and':
        memory[pointer] = int(memory[pointer] and transVars(program[i+1]))
        i += 1
    elif instruction == 'or':
        memory[pointer] = int(memory[pointer] or transVars(program[i+1]))
        i += 1
    elif instruction == 'xor':
        memory[pointer] = int(bool(memory[pointer]) ^ bool(transVars(program[i+1])))
        i += 1
    # Flow
    elif instruction == 'goto':
        try: i = markers[transVars(program[i+1])]-1
        except KeyError: error("Unknown marker %d"%transVars(program[i+1]))
    elif instruction == 'qoto':
        i = markers[transVars(program[i+2])]-1 if memory[pointer] == transVars(program[i+1]) else markers[transVars(program[i+3])]-1
        #except KeyError: error("Unknown marker %d"%(transVars(program[i+2]) if not transVars(program[i+2]) in markers else transVars(program[i+3])))
    elif instruction == 'wait': input()
    # I/O
    elif instruction == 'input':
        stdin = input()
        try: memory[pointer] = number(stdin) if len(stdin) > 0 else 0
        except: error("Cannot convert %s to number"%stdin)
    elif instruction == 'inputc':
        stdin = input()
        memory[pointer] = ord(stdin[0]) if len(stdin) > 0 else 0
    elif instruction == 'read':
        try:
            with open(program[i+1], 'rb') as f: memory[pointer] = f.read()[transVars(program[i+2])]
        except FileNotFoundError: error("File not found: %s"%program[i+1])
        except IndexError: error("Specified byte is beyond the end of the file: %s"%transVars(program[i+2]))
        i += 2
    elif instruction == 'size':
        with open(program[i+1], 'rb') as f: memory[pointer] = len(f.read())
        i += 1
    elif instruction == 'print': print('nil' if memory[pointer] == None else memory[pointer])
    elif instruction == 'printc':
        try: print(chr(memory[pointer]), end="", flush=True)
        except TypeError: error("Cannot convert nil to character")
    elif instruction == 'write':
        with open(program[i+1], 'w') as f: f.write(chr(memory[pointer]))
        i += 1
    elif instruction == 'awrite':
        with open(program[i+1], 'a') as f: f.write(chr(memory[pointer]))
        i += 1
    elif instruction == 'writeb':
        with open(program[i+1], 'wb') as f: f.write(bytearray([memory[pointer]]))
        i += 1
    elif instruction == 'awriteb':
        with open(program[i+1], 'ab') as f: f.write(bytearray([memory[pointer]]))
        i += 1
    elif instruction == 'mem':
        print('|'+'|'.join([str(x[1]).replace('None',' ') for x in sorted(memory.items())])+'|')

    elif instruction == 'stop': breakf
    elif instruction.startswith(":"): pass
    else:
        try: memory[pointer] = transVars(instruction)
        except: error("Unknown instruction %s"%instruction)
    if not pointer in memory: memory[pointer] = None
    i += 1