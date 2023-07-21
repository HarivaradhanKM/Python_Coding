start_num = 2
row = 4
Column = row

for i in range(1, row+1):
    for j in range(0, Column):
        print(end="")
    for j in range(0, i*2):
        print(start_num, end=" ")
        start_num = start_num + 1
    print()