plik = open("punkty.txt").read().split("\n")


def pierwsza (a):
    for x in range(2,a//2):
        if a % x == 0:
            return False
    return True

counter = 0

for l in plik:
    l = l.split(" ")
    if pierwsza(int(l[0])) and pierwsza(int(l[1])):
        counter+=1

print(counter)