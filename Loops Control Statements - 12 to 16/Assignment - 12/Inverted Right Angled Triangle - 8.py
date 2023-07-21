n = int(input())
k = 2*n-1
j = 0
for i in range(1, n+1):
    left_space = "  " * j 
    print(left_space + "* " * k)
    k = k-2
    j = j+2