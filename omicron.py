import sys
if len(sys.argv) > 1:
    program = [c.strip() for c in open(sys.argv[1], 'r').read().split()]
    memory = {}
    def error(m):
        global ok
        print("ERROR: instruction %d: %s"%(i,m))
        ok = 0
    def number(n):
        return float(n) if ('.' in str(n)) else int(n)
    def mem(instruction):
        for cell in memory: instruction = instruction.replace("@"+str(cell), str(memory[cell]))
        return number(instruction)
    ok = 1
    pointer = 0
    i = 0
    markers = {}
    for m in range(0, len(program)):
        if program[m].startswith(":"): markers[int(program[m][1:])] = m
    while True:
        try:
            try: instruction = program[i]
            except IndexError:
                error("Missing stop")
                break
            # Pointer
            if instruction == '>': pointer += 1
            elif instruction == '<': pointer -= 1
            elif instruction == '>>':
                pointer += mem(program[i+1])
                i += 1
            elif instruction == '<<':
                pointer -= mem(program[i+1])
                i += 1
            elif instruction == '~':
                pointer = mem(program[i+1])
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
                try: memory[pointer] /= mem(program[i+1])
                except ZeroDivisionError: error("Cannot divide by zero")
                i += 1
            elif instruction == '//':
                try: memory[pointer] //= mem(program[i+1])
                except ZeroDivisionError: error("Cannot divide by zero")
                i += 1
            elif instruction == '^':
                memory[pointer] **= mem(program[i+1])
                i += 1
            elif instruction == '%':
                try: memory[pointer] %= mem(program[i+1])
                except ZeroDivisionError: error("Cannot mod by zero")
                i += 1
            elif instruction == '\\':
                memory[pointer] = memory[pointer]**(1/mem(program[i+1]))
                i += 1
            # Flow
            elif instruction == 'goto':
                try: i = markers[mem(program[i+1])]-1
                except KeyError: error("Unknown marker %d"%mem(program[i+1]))
            elif instruction == 'qoto':
                try: i = markers[mem(program[i+1])]-1 if not memory[pointer] == 0 else markers[mem(program[i+2])]-1
                except KeyError: error("Unknown marker %d"%mem(program[i+1]))
            elif instruction == 'wait': input()
            # I/O
            elif instruction == 'input':
                stdin = input()
                try: memory[pointer] = number(stdin) if len(stdin) > 0 else 0
                except: error("Cannot convert %s to number"%stdin)
            elif instruction == 'inputc':
                stdin = input()
                memory[pointer] = ord(stdin[0]) if len(stdin) > 0 else 0
            elif instruction == 'print': print(memory[pointer])
            elif instruction == 'printc': print(chr(memory[pointer]), end="", flush=True)

            elif instruction == 'stop': break
            elif instruction.startswith(":"): pass
            else:
                try:
                    memory[pointer] = mem(instruction)
                except:
                    error("Unknown instruction %s"%instruction)
            if not ok: break
            i += 1
        except KeyboardInterrupt:
            print("Execution halted by user")
            break
    if not ok: input()
else:
    print("Missing input file")
    input()