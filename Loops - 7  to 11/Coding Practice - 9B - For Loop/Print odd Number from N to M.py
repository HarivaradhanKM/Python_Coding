M = 5
N = 15

if M > N:
    M,N = N,M
for i in range(N, M-1, -1):
    if i % 2 == 1:
        print(i, end=" ")