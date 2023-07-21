n = 4
start_n = 0
for number in range(1, n+1):
    start_n += number
for row in range(n):
    each_row = ""
    left_space = " "*(2*row)
    for column in range(n-row):
        each_row = each_row + str(start_n) + " "
        start_n = start_n - 1 
    each_row = left_space + each_row
    print(each_row)