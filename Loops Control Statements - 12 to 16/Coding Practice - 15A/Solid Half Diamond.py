n = 5
for i in range(1, n):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
    
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()