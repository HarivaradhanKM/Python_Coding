n = 5

for i in range(n):
    for j in range(i + 1):
        print(i+1, end=" ")
    print()

for i in range(n-1, 0, -1):
    for k in range(0, i):
        print(i, end=" ")
    print()