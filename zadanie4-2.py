plik = open("punkty.txt").read().split("\n")

def funk(a):
    tab = []
    for x in a:
        if x not in tab:
            tab.append(x)
    tab.sort()
    return tab

counter = 0

for l in plik:
    l = l.split()
    if funk(l[0]) == funk(l[1]):
        counter+=1

print(counter)