largestP = 0

for i in range(100, 1000):
    for x in range(100, 1000):
        current = str(i * x)
        if current == current[::-1] and int(current) > largestP:
            largestP = int(current)
        print(current)
print(largestP)
