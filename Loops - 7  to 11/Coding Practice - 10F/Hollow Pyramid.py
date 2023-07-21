N = 6

for i in range(1, N+1):
    left_space = " " * (N-i)
    if i > 2 and i < N :
        hollow_space = "  " * (i - 2)
        star = "* " + hollow_space + "*"
        print(left_space + star)
    else:
        star = "* " * i
        print(left_space + star)