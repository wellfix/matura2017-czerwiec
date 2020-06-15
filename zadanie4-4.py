plik = open("punkty.txt").read().split("\n")

def wew(x ,y):
    if x > -5000 and x < 5000 and y > -5000 and y < 5000:
        return True
    else:
        return False


def zew(x ,y):
    if x >= -5000 and x <= 5000 and (y == -5000 or y == 5000):
        return True
    elif y >= -5000 and y <= 5000 and (x == -5000 or x == 5000):
        return True
    else:
        return False


a = 0
b = 0
c = 0

for l in plik:
    l = l.split()
    if wew(int(l[0]), int(l[1])):
        a+=1
    elif zew(int(l[0]), int(l[1])):
        b+=1
    else:
        c+=1

print(a)
print(b)
print(c)