def parseInput():
    with open("day1part1.txt") as text:
        leftList = []
        rightList = []
        for line in text:
            num1, num2 = line.split()
            leftList.append(num1)
            rightList.append(num2)
        return leftList, rightList

def part1():
    leftList, rightList = parseInput()
    leftList.sort()
    rightList.sort()
    print(leftList, rightList)
    answer = 0
    for i in range(len(leftList)):
        answer += abs(int(leftList[i]) - int(rightList[i]))
    return answer

def part2():
    leftList, rightList = parseInput()
    d = {}
    answer = 0
    for num in map(int, rightList):
        d[num] = d.get(num, 0) + 1
    for num in map(int, leftList):
        answer += num * d.get(num, 0)
    return answer
    

print(part1())
print(part2())