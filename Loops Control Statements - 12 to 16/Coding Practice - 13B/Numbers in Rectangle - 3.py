M = 2 #rows
N = 3 # columns 
Start_Number = M * N
for i in range(1, M+1):
    for j in range(1, N+1):
        print(Start_Number, end=" ")
        Start_Number = Start_Number - 1
    print()