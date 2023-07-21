Num = 5

for i in range(Num):
    for j in range(Num):
        if (j == 0) or (i == 0) or (i+j == (Num-1)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()