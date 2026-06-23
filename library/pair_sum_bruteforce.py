n = int(input())
a = list(map(int, input().split()))
counter = 0
for i in range(n):
        for j in range(i+1, n):
                if a[i] + a[j] == 0:
                        counter+=1
print(counter)
