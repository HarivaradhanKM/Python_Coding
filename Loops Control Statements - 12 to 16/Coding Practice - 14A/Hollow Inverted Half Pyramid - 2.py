n = 5

for i in range(1, n+1):
    for j in range(1, n+1):
        if (j == 1) or (j+i == (n+1)) or (i == 1):
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()