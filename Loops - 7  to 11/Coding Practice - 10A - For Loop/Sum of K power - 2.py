N = "24753"

K = len(N) 

Sum = 0
for i in range(K):
    Sum = Sum + (int(N[i]) ** K)
print(Sum)