searching = True
num = 0
numRange = 20


while searching:
    num += numRange
    count = 1
    for i in range(1, numRange):
        if (num / i) % 1 == 0:
            count += 1
    if count == numRange:
        searching = False
        print("Number is", num)
        print("Divisible by", count, "numbers")

