n = int(input())
counter = 0
pole = []
for i in range(n):
        i = input()
        pole.append(i)
for cislo in range(len(pole) - 1):
        if pole[cislo]=! pole[cislo+1]:
                counter+=1
print(counter + 1)
