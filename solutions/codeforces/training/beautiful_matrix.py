import sys
matrix = []
for i in range(5):
     cislo = list(map(int,input().split()))
     matrix.append(cislo)
for j, riadok in enumerate(matrix):
     for j, cislo in enumerate(riadok):
          if cislo == 1:
               print(abs(i-2) + abs(j-2))