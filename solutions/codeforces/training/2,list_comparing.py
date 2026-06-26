n = input()
p = input()
result = ""
for i in range(len(n)):
        if n[i] != p[i]:
                result += "1"
        else:
                result += "0"
print(result)
                
