n = 7

if n == 1:
    print(". ")
else:
    print(". ")
    
    for i in range(1, n-1):
        center_zeros = "0 " * (i-1)
        row = ". " + center_zeros + "."
        print(row)
    print(". " *n)