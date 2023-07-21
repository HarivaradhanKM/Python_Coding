s = 8
n = 4
k = 0
for i in range(1,n+1):
    k = k+i 
m = k+s-1

for i in range(n):
    for j in range(n-i):
        print(m, end=" ")
        m = m-1
    print()