s = 2
n = 3

for i in range(1, n+1):
    for j in range(1, n+1):
        if (i == n) or (i == 1) or (j == n) or (j == 1):
            print(s, end=" ")
            s = s+1
        else:
            print(" ", end=" ")
            s = s+1
    print()