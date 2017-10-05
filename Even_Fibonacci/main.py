num = 2
nextNum = 0
prevNum = 1
evenNums = 2

while num < 4000000:
    nextNum = num + prevNum

    # print(prevNum, num, nextNum)

    prevNum = num
    num = nextNum

    if nextNum % 2 == 0:
        evenNums += nextNum
        print(evenNums)

print(evenNums)