n = 3
for k in range(n):
    for m in range(k):
        print("* ", end="")
    for m in range(k+1, 0,-1):
        print("* ", end="")
    print()