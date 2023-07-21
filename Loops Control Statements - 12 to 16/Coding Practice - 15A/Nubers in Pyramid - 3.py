n = 5

for i in range(1, n+1):
    zero = "0 " * (n-i)
    number = "1 " * (2*i-1)
    print(zero+number+zero)