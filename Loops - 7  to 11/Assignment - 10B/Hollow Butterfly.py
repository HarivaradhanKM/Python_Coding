N = 4
for i in range(1, N+1):
    space = 2*N-2*i 
    for j in range(1,i+1):
        if (j==1 or j==i):
            print("*", end=" ")
        else:
            print("  ", end="")
    for j in range(space):
        print("  ", end="")
    for j in range(1, i+1):
        if (j==1 or j==i):
            print("*", end=" ")
        else:
            print("  ", end="")
    print()

for i  in range(N,0,-1):
    space = 2*N-2*i 
    for j in range(1, i+1):
        if (j==1 or j==i):
            print("*", end=" ")
        else:
            print("  ", end="")
    for j in range(space):
        print("  ", end="")
    for j in range(1, i+1):
        if (j==1 or j==i):
            print("*", end=" ")
        else:
            print("  ", end="")
    print()
            
            