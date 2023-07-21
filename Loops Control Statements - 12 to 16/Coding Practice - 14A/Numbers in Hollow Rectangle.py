n = 4
m = 3
for i in range(1, n+1):
    for j in range(1, m+1):
        if (i == n) or (i == 1) or (m == j) or (j == 1):
            print(j+6, end=" ")
        else:
            print(" ", end=" ")
    print()