size = 6

for i in range(size, 0, -1):
    for j in range(size-i, 0, -1):
        print(" ", end="")
    for k in range(1, i + 1):
        print(i, end="")
    print()