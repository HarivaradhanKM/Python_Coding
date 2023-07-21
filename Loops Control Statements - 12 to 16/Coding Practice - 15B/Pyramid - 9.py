n = 5

for i in range(1, n+1):
    dot = ". " * (n-i)
    zero = "0 " * (2*i-1)
    print(dot+zero+dot)