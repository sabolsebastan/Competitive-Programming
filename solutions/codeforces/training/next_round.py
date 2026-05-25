n, k = map(int, input().split())
skore = list(map(int, input().split()))
pocitadlo = 0

for x in skore:
    if x >= skore[k-1] and x > 0:
        pocitadlo += 1

print(pocitadlo)