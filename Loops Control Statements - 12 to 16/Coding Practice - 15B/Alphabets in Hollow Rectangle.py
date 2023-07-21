row = 4
column = 6
Alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Count = 0 
for i in range(row):
    a = ""
    for j in range(column):
        if (i == 0) or (i == row-1):
            a = a + Alphabets[Count] + " "
        elif (j == 0):
            a = a + Alphabets[Count] + " " * (2 * column - 3) + Alphabets[column + Count - 1]
        Count = Count + 1 
    print(a)
    