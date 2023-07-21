n = 3
k = n-1
for i in range(1, n+1):
    spaces = " " * k 
    starts = "* " * i 
    print(spaces + starts)
    k = k - 1 

k = n 
for i in range(1, n):
    spaces = " " * i 
    starts = "* " * (k - i)
    print(spaces + starts)