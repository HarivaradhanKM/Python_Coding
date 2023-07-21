n = 4
m = 5
start_number = 1
for i in range(1, n+1):
    for j in range(1, m+1):
        if (i == n) or (i == 1) or (m == j) or (j == 1):
            print(start_number, end=" ")
            start_number = start_number + 1
        else:
            print(" ", end=" ")
            start_number = start_number + 1
    print()