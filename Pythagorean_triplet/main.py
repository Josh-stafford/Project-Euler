import math
a = 0
searching = True

while searching and a <= 400:
    a += 1
    for b in range(a+1, 1000):
        cSqr = (a*a) + (b*b)
        c = math.sqrt(cSqr)

        if a+b+c == 1000:
            print(a*b*c)
            searching = False
# print(a, b, c)