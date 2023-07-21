M = 2
N = 9
count = 0
for M in range(M, N+1):
    for i in range(1, M+1):
        if (M % i == 0):
            count += 1
    if count > 2:
        print(M)
    count = 0
    