from math import ceil

def work():
    num = 0
    goal = int(input())
    while True:
        divisors = 2
        num += 1
        triangle = 0

        for i in range(1, num+1):
            triangle += i

        for x in range(1, int(ceil(triangle/2))):
            if float(triangle)/x % 1 == 0:
                divisors += 1
            if divisors > goal:
                return triangle