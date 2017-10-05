sum = 0
sqrSum = 0

for i in range(1,101):
    sum += i
    sqrSum += (i*i)

sum *= sum

print(sum - sqrSum)
