N = 12
K = 2
count = 0
kth_factor = False
factor = N 
for i in range(1, N+1):
    if (N % factor == 0):
        count = count + 1 
        if count == K:
            print(factor)
            kth_factor = True
    factor = factor - 1 
if count < K:
        print("1")

