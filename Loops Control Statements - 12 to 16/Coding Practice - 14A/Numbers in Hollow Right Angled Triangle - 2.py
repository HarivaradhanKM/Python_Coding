n = 6

for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        if (i+j == n+1) or (i == 1) or (j == 1):
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()