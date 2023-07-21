r = 6
for i in range(1, r):
    for j in range(1, 2*r):
        if (i+j == r+1) or (j-i == r-1):
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(1, r+1):
    for j in range(1, 2*r):
        if (i==j) or (i+j==2*r):
            print("*", end="")
        else:
            print(" ", end="")
    print()
