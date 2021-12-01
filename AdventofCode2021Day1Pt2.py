ComparisonList = []
IncreaseCount = 0
def Increase(List):
    if len(List) < 4:
        return False
    else:
        Determiner1 = sum(List[:3])
        Determiner2 = sum(List[1:])
        ComparisonList.pop(0)
    if Determiner2 > Determiner1:
        return True
    
with open('AdventofCode2021Day1Input.txt', "r") as f:
    Input = f.readlines()
    for line in Input:
        Newline = line.split()
        ComparisonList.append(int(Newline[0]))
        if Increase(ComparisonList) == True:
            IncreaseCount += 1
    
print(IncreaseCount)
    
