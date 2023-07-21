start_num = 7
row = 5
Column = (2*row) - 1 

for i in range(0, row):
    for j in range(0, Column-i-row):
        print(end=" ")
    for j in range(0, i+1):
        print(j+start_num, end=" ")
    print()