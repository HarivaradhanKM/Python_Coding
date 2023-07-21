N = 10
K = 5
Sum = 0
for i in range(1,K+1):
    Sum = Sum+i 
m = Sum+N-1

for i in range(K):
    for j in range(i+1):
        print(m, end=" ")
        m = m-1
    print()