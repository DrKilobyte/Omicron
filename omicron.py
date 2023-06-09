import sys, math, random
if len(sys.argv) > 1:
    try:
        program = [c.strip() for c in open(sys.argv[1], 'r').read().split()]
    except FileNotFoundError:
        print("File not found: %s"%sys.argv[1])
        sys.exit()
    memory = {}
    def error(m):
        global ok
        print("ERROR: instruction %d: %s"%(i,m))
        ok = 0
    def number(n):
        return float(n) if ('.' in str(n)) else int(n)
    def mem(instruction):
        while '@' in instruction:
            for cell in memory: instruction = instruction.replace("@"+str(cell), str(memory[cell]))
        return number(instruction)
    ok = 1
    pointer = 0
    i = 0
    markers = {}
    # Imports
    for m in range(0, len(program)):
        try:
            if program[m].startswith("!"):
                with open(program[m][1:]) as f:
                    program[m:m] = f.read().split()
                    program.pop(m+len(f.read().split())-1)
        except FileNotFoundError: error("File not found: %s"%program[m][1:])
    # Markers
    for m in range(0, len(program)):
        try:
            if program[m].startswith(":"): markers[int(program[m][1:])] = m
        except ValueError: error("Marker must be a number: :%s"%program[m][1:])
    while i < len(program):
        try:
            instruction = program[i]
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
                if mem(program[i+1]) > 1: memory[pointer] = math.log(memory[pointer], mem(program[i+1]))
                else: error("Log base must be 2 or greater")
                i += 1
            elif instruction == 'fact':
                try: memory[pointer] = math.factorial(mem(program[i+1]))
                except: error("Cannot convert %s to number"%program[i+1])
                i += 1
            elif instruction == 'abs': memory[pointer] = abs(memory[pointer])
            elif instruction == 'not': memory[pointer] = int(not memory[pointer])
            elif instruction == 'rand':
                try:
                    memory[pointer] = random.randint(mem(program[i+1]), mem(program[i+2]))
                except:
                    try: error("Cannot convert %s to number"%program[i+1])
                    except: error("Cannot convert %s to number"%program[i+2])
                i += 2
            elif instruction == 'pi': memory[pointer] = math.pi
            elif instruction == 'e': memory[pointer] = math.e
            # Comparison
            elif instruction == 'eq':
                memory[pointer] = int(memory[pointer]==mem(program[i+1]))
                i += 1
            elif instruction == 'gt':
                memory[pointer] = int(memory[pointer]>mem(program[i+1]))
                i += 1
            elif instruction == 'gte':
                memory[pointer] = int(memory[pointer]>=mem(program[i+1]))
                i += 1
            elif instruction == 'lt':
                memory[pointer] = int(memory[pointer]<mem(program[i+1]))
                i += 1
            elif instruction == 'lte':
                memory[pointer] = int(memory[pointer]<=mem(program[i+1]))
                i += 1
            # Flow
            elif instruction == 'goto':
                try: i = markers[mem(program[i+1])]-1
                except KeyError: error("Unknown marker %d"%mem(program[i+1]))
            elif instruction == 'qoto':
                try: i = markers[mem(program[i+1])]-1 if not memory[pointer] == 0 else markers[mem(program[i+2])]-1
                except KeyError: error("Unknown marker %d"%(mem(program[i+1]) if not mem(program[i+1]) in markers else mem(program[i+2])))
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
                    with open(program[i+1], 'rb') as f: memory[pointer] = f.read()[mem(program[i+2])]
                except FileNotFoundError:
                    error("File not found: %s"%program[i+1])
                except IndexError:
                    error("Specified byte is beyond the end of the file: %s"%mem(program[i+2]))
                i += 2
            elif instruction == 'size':
                with open(program[i+1], 'rb') as f: memory[pointer] = len(f.read())
                i += 1
            elif instruction == 'print': print(memory[pointer])
            elif instruction == 'printc': print(chr(memory[pointer]), end="", flush=True)
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