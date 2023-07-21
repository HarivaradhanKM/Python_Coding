start_num = 10
row = 5
Column = row

for i in range(0, row):
    for j in range(0, Column):
        print(end="")
    for j in range(0, i+1):
        print(start_num, end=" ")
        start_num = start_num + 1
    print()