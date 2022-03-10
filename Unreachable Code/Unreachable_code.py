data = 'UnreachableCode.txt'
lines = 0 
c = 0 
with open(data, "r") as t:
    line = t.readline()
    while line:
        lines+=1
        line = t.readline()
with open(data, "r") as t:
    line = t.readline()
    while line:
        c+1
        if line.startswith("if"):
            print('if statement')
            do = t.readline()
            if do.find('return'):
                print('out')
                if lines > c:
                    print("Unreachable Code Detected")
        line = t.readline()

with open(data) as file:
    for line in file:
        pass
    last_line = line
with open(data) as fp:
    line = fp.readline()
    c = 1
    while line:
        if line.startswith("return"):
            if line != last_line:
                print(line)
                print('the next code is unreachable')
        line = fp.readline()
        c+1