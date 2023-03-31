import sys
if len(sys.argv) > 1:
    program = [c.strip() for c in open(sys.argv[1], 'r').read().split()]
    memory = {}
    number = lambda n: int(float(n)) if int(float(n)) == float(n) else float(n)
    def mem(instruction):
        for cell in memory: instruction = instruction.replace("@"+str(cell), str(memory[cell]))
        return number(instruction)
    pointer = 0
    i = 0
    while True:
        instruction = program[i]
        # Set memory
        if instruction == 'set':
            memory[pointer] = mem(program[i+1])
            i += 1
        # Pointer
        elif instruction == '>': pointer += 1
        elif instruction == '<': pointer -= 1
        elif instruction == '>>':
            pointer += mem(program[i+1])
            i += 1
        elif instruction == '<<':
            pointer -= mem(program[i+1])
            i += 1
        elif instruction == ':':
            pointer == mem(program[i+1])
            i += 1
        # Arithmetic
        elif instruction == '++': memory[pointer] += 1
        elif instruction == '--': memory[pointer] -= 1
        elif instruction == '+':
            memory[pointer] += mem(program[i+1])
            i += 1
        elif instruction == '-':
            memory[pointer] -= mem(program[i+1])
            i += 1
        elif instruction == '*':
            memory[pointer] *= mem(program[i+1])
            i += 1
        elif instruction == '/':
            memory[pointer] //= mem(program[i+1])
            i += 1
        elif instruction == '^':
            memory[pointer] **= mem(program[i+1])
            i += 1
        elif instruction == '%':
            memory[pointer] %= mem(program[i+1])
            i += 1
        elif instruction == '\\':
            memory[pointer] = memory[pointer]**(1/mem(program[i+1]))
            i += 1
        # Flow
        elif instruction == 'goto':
            i = mem(program[i+1])-1
        elif instruction == 'qoto':
            i = mem(program[i+1])-1 if not memory[pointer] == 0 else mem(program[i+2])-1
        elif instruction == 'wait': input()
        # I/O
        elif instruction == 'input':
            stdin = input()
            memory[pointer] = mem(stdin) if len(stdin) > 0 else 0
        elif instruction == 'ascii':
            stdin = input()
            memory[pointer] = ord(stdin[0]) if len(stdin) > 0 else 0
        elif instruction == 'print': print(memory[pointer], end="", flush=True)
        elif instruction == 'char': print(chr(memory[pointer]), end="", flush=True)

        elif instruction == 'stop': break
        i += 1
else:
    print("Missing input file")