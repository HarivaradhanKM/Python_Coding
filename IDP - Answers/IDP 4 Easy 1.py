def print_right_angled_triangle(n):
    for i in range(1, n+1):
        each_row = ""
        for j in range(i):
            if j % 2 == 0:
                each_row += "1" + " "
            else:
                each_row += "0" + " "
        print(each_row)