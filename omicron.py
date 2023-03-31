import sys
program = [c.strip() for c in open(sys.argv[1], 'r').read().split()]
memory = {}
def mem(c):
    global memory
    for cell in memory: c = c.replace("@"+str(cell), str(memory[cell]))
    return int(c)
pointer = 0
i = 0
while True:
    command = program[i]
    # Set memory
    if command == 'zero': memory[pointer] = 0
    elif command == 'set':
        memory[pointer] = mem(program[i+1])
        i += 1
    # Pointer
    elif command == '>': pointer += 1
    elif command == '<': pointer -= 1
    elif command == '>>':
        pointer += mem(program[i+1])
        i += 1
    elif command == '<<':
        pointer -= mem(program[i+1])
        i += 1
    elif command == ':':
        pointer == mem(program[i+1])
        i += 1
    # Arithmetic
    elif command == '++': memory[pointer] += 1
    elif command == '--': memory[pointer] -= 1
    elif command == '+':
        memory[pointer] += mem(program[i+1])
        i += 1
    elif command == '-':
        memory[pointer] -= mem(program[i+1])
        i += 1
    elif command == '*':
        memory[pointer] *= mem(program[i+1])
        i += 1
    elif command == '/':
        memory[pointer] //= mem(program[i+1])
        i += 1
    elif command == '^':
        memory[pointer] **= mem(program[i+1])
        i += 1
    elif command == '%':
        memory[pointer] %= mem(program[i+1])
        i += 1
    elif command == '\\':
        memory[pointer] = memory[pointer]**(1/mem(program[i+1]))
        i += 1
    # Flow
    elif command == 'goto':
        i = mem(program[i+1])-1
    elif command == 'qoto':
        i = mem(program[i+1])-1 if memory[pointer] == 0 else mem(program[i+2])-1
    elif command == 'wait': input()
    # I/O
    elif command == 'input':
        stdin = input()
        memory[pointer] = int(stdin) if len(stdin) > 0 else 0
    elif command == 'ascii':
        stdin = input()
        memory[pointer] = ord(stdin[0]) if len(stdin) > 0 else 0
    elif command == 'print': print(memory[pointer])
    elif command == 'char': print(chr(memory[pointer]))

    elif command == 'stop': break
    i += 1