M = 2
N = 7

Sum = 1

for odd in range(M, N+1):
    if (odd % 2 != 0):
        Sum *= odd
print(Sum)