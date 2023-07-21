n = 5

for i in range(1, n+1):
    left_space = " " * (n-i)
    if i > 2 and i < n :
        hollow_space = "  " * (i-2)
        star = "* " + hollow_space + "*"
        print(left_space + star)
    else:
        star = "* " * i
        print(left_space + star)