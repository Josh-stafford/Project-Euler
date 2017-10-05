primes = 1
num = 1
working = True

while primes < 10001:
    num += 2
    isntPrime = False
    if num % 2 == 0:
        isntPrime = True
    else:
        for i in range(3, num):
            if(num / i) % 1 == 0:
                isntPrime = True

    if not isntPrime:
        primes += 1
        if primes % 500 == 0:
            print(num, primes)

print(num)
