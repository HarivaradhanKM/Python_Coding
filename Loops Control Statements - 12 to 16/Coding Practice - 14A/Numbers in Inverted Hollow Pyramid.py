n = 5
s = 7
for i in range(1, n+1):
    for j in range(1, i):
        print(" ", end="")
    for j in range(1, n+1):
        if (i == 1) or (j == 1) or (j+i == (n+1)):
            print(((j+s)-1), end=" ")
        else:
            print(" ", end=" ")
    print()