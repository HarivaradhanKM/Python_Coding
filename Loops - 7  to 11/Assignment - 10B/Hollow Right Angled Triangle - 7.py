N = 4
for row in range(N):
    for col in range(N):
        if (row == 0):
            print("+", end=" ")
        elif (col == N-1 or row == col):
            print("*", end=" ")
        else:
            print(end="  ")
    print()