from math import ceil

num = 600851475143
largestPrime = 0

for i in range(2, ceil(num/2)):
    isntPrime = False
    if i % 2 == 0:
        isntPrime = True
    else:
        for x in range(3,i):
            if (i / x) %1 == 0:
                isntPrime = True
    if isntPrime == False:
        if (num / i) % 1 == 0 and i > largestPrime:
            largestPrime = i
            print(largestPrime)



