N = 5
Decrease = N
for i in range (1,N+1):
    if(i==1):
        print ("* " * N)
    else:
        Decrease = Decrease - 1
        print("+ " * Decrease)