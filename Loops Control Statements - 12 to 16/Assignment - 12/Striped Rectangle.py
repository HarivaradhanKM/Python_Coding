M = 5 #row 
N = 7 #columns

for i in range(M):
    for j in range(N):
        if (i % 2 == 0):
            print("+", end=" ")
        else:
            print("-", end=" ")
    print()