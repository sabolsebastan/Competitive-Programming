import sys

cisla = sys.stdin.read().split()

for i in range(len(cisla)):
    if cisla[i] == "kod:":
        print(cisla[i + 1])
        break