import re
commac= 0
with open("Parameters.txt", "r") as t:
    for line in t:
        if line.startswith("def"):
            commac = (len(re.findall(",", line))) 
        if commac in range (0,3):
            print(True)
        else: 
            print(False)