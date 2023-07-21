T = 10
M = 20
N = 200

Sum = 0
for counter in range(M, N+1):
    if (counter % T == 0):
        Sum += counter
print(Sum)