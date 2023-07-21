Num = 5

for i in range(1, Num+1):
    for j in range(1, 2*Num):
        if (i==1 and j%2 != 0) or i == j or i+j == Num * 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()