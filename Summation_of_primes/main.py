from math import ceil

primeSum = 2
num = 3
count = 0

while num < 2000000:
    count+=1
    isntPrime = False

    for x in range(3, ceil(num/2)):
        if x % 2 != 0:
            if(float(num) / float(x)) % 1 == 0:
                isntPrime = True
                break

    if isntPrime == False:
        primeSum += num

    if count % 10000 == 0:
        print(count)

    num += 2

print(primeSum)