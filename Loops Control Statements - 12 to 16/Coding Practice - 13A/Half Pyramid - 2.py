Num = 5
Start_Number = 1
for i in range(1,Num+1):
    for j in range(1, i+1):
        print(Start_Number, end=" ")
        Start_Number = Start_Number + 1
    print()