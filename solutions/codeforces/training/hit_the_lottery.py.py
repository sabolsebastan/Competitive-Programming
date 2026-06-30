n = int(input())
nominals = [100, 20, 10, 5, 1]
counter = 0
final = 0
for i in nominals:
    pocet_bankoviek = n // i
    counter += pocet_bankoviek
    n = n % i 
print(counter)
