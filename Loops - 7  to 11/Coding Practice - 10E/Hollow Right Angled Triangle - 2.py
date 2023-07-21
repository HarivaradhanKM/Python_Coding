n = 5

for i in range(n+1):
    print("_", end="")
print()
for i in range(n):
    print("|", end="")
    print(" " * (n-i-1), end= "")
    print("/")