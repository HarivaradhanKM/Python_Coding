n = int(input())
for i in range(1, n+1):
    if (i == 1) or (i == 2):
        print(("  " * (n-i)) + (str(i) + " ") * i)
    else:
        print(("  " * (n-i)) + (str(i) + " ") +("  " * (i-2)) + str(i))
        
for i in range(1, n):
    if (i == n-1):
        print(("  " * i) + (str(1) + " ") * 1)
    elif (i == (n-2)):
        print(("  " * i) + (str(2) + " ") * 2)
    else:
        print(("  " * i) + (str(n-i) + " ") + ("  " * (n-i-2)) + (str(n-i)+" ")) 
        