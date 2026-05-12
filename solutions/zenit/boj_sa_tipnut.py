import sys
# 1. Načítame všetko zo vstupu a rozdelíme na kúsky
data = list(map(int, sys.stdin.read().split()))
# 2. Použijeme tú divnú premennú zo zadania (povinná podmienka!)
clslo = sum(data)
# 3. Vypíšeme čokoľvek, čo nie je súčet (súčet + 1 je najistejšia cesta)
print(clslo + 1)

#používaj ak treba niečo spočitať alebo odčítať a vytvoriť vystup...
