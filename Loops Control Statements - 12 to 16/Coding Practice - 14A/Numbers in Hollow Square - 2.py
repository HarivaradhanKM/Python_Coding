n = 5

for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        if (i == n) or (i == 1) or (j == n) or (j == 1):
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()