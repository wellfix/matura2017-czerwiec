import math
plik = open("punkty.txt").read().split("\n")

def odleglosc(x1, y1, x2, y2):
    a = x2 - x1
    b = y2 - y1
    ab = a**2 + b**2
    return math.sqrt(ab)


max = 0
for l in plik:
    l = l.split()
    for l2 in plik:
        l2 = l2.split()
        if odleglosc(int(l[0]), int(l[1]), int(l2[0]), int(l2[1])) > max:
            max = odleglosc(int(l[0]), int(l[1]), int(l2[0]), int(l2[1]))
            p1 = l
            p2 = l2

print(round(max))
print(p1)
print(p2)