ComparisonList = []
IncreaseCount = 0
def Increase(List):
    if len(List) == 1:
        return False
    else:
        Determiner = List[1] - List[0]
        ComparisonList.pop(0)
    if Determiner > 0:
        return True
    
with open('AdventofCode2021Day1Input.txt', "r") as f:
    Input = f.readlines()
    for line in Input:
        Newline = line.split()
        ComparisonList.append(int(Newline[0]))
        if Increase(ComparisonList) == True:
            IncreaseCount += 1
    
print(IncreaseCount)
    
