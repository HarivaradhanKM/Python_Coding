m = 3 #row
n = 6 #column
k = m*n #starting Number
for i in range(1, m+1):
    for j in range(1, n+1):
        if (i == m) or (i == 1) or (n == j) or (j == 1):
            print(k, end=" ")
            k = k-1
        else:
            print(" ", end=" ")
            k = k-1
    print()