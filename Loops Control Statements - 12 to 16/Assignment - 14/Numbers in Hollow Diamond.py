n = 5

for i in range(1, n+1):
    if i == 1:
        print(" " * (n-1) + str(i))
    else:
        print(" " * (n-i) + str(1) + " " + "  " * (i-2) + str(i) ) 
for j in range(1, n):
    if j == n-1:
        print(" " * (n-1) + str(1))
    else:
        print(" " * j + str(1) + " " + "  " * (n-(j+2))+ str(n-j)) 
