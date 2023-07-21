N = 25
T = 5

Sum = 0

for i in range(1, N+1):
    if (i % T == 0):
        Sum = (N/T)
print(int(Sum))