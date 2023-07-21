M = 2
N = 7

Sum = 1
for i in range(M, N+1):
    if (i % 3==0):
        Sum = (i * Sum)
print(Sum)