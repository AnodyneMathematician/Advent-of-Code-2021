HorizontalPosition = 0
Depth = 0
Aim = 0
with open("AdventofCode2021Day2Input.txt") as f:
    Input = f.readlines()
    NewList = [line.split() for line in Input]
    NewList = [[line[0],int(line[1])] for line in NewList]
    for line in NewList:
        if line[0] == "forward":
            HorizontalPosition += line[1]
            Depth += line[1]*Aim
        elif line[0] == "up":
            Aim += -line[1]
        elif line[0] == "down":
            Aim += line[1]
            
print(HorizontalPosition*Depth)
