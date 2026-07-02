n = int(input())
timy = []
for i in range(n):
        h, a = map(int, input().split())
        timy.append((h,a))
        
counter = 0
for i in range(n):
        for j in range(n):
                if j != i and timy[i][0] == timy[j][1]:
                        counter+=1
print(counter)
