n = 5
for i in range(1, n+1):
    if (i==1):
        print("1")
    elif (i==n):
        space = "  " * (n-2)
        print(str(i)+" " +space + str(i))
    else:
        space = "  " * (i-2)
        print(str(i)+" " +space + str(i))
        
a = n-1

for i in range(2, n+1):
    if i==n:
        print("1")
    else:
        space = "  " * (n-i-1)
        print(str(a)+" " + space + str(a))
        a = a - 1