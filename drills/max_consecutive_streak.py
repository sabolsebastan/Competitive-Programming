n = int(input())
i = map(int,input().split())
streak = 0
maximum = 0
for i in range(n):
  
  for cislo in i:
    if cislo == 1:
      streak+=1
    else:
      if maximum = max(maximum, streak):
        streak = 0
      else:
        streak += maximum
  print(maximum)
