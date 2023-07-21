size = game
lenth = len(size)
for row in range(lenth+1, 0, -1):
    for col in range(row-1):
        print(size[col], end="")
    print()