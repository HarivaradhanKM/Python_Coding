N = 6
C = 2 * N;

for row in range(1, N+1):
    for col in range(1, C+1):
        if (row==N or col==1 or col==C or row==col or (row + col == C+1)):
            print("* ",end="")
        else:
            print(" ",end=" ")
    print()