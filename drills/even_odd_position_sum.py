n = int(input())
a = list(map(int, input().split()))
parne = sum(a[1::2])
neparne = sum(a[::2])
if parne > neparne:
        print("EVEN")
elif parne < neparne:
        print("ODD")
else:
        print("EQUAL")
