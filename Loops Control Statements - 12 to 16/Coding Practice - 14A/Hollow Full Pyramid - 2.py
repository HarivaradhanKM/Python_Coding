n = 5

for i in range(1, n+1):
    left_space = " " * (n-i)
    if i > 2 and i < n:
        hollow_space = " " * (2*(i-2))
        number = "1 " + hollow_space + (str(i) + " ")
        print(left_space + number)
    else:
        number = ""
        for j in range(1, i+1):
            number = number + (str(j) +" ")
        print(left_space + number)