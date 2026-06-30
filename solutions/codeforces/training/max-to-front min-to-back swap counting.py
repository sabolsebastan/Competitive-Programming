n = int(input())
a = list(map(int, input().split()))
maximum = max(a)
i_max = a.index(maximum)
minimum = min(a)
i_min = n - 1 - a[::-1].index(minimum)
cost = i_max + (n - 1 - i_min)
if i_max > i_min:
    cost -= 1
print(cost)
