n = 4
r = 2*n-1
for i in range(1, (r)+1):
        if (i == 1) or (i == n) or (i == r):
            star = "* " * n
            print(star)
            count = 1
        elif (i == n+count):
            print("  "+ space + "* ")
            count = count + 1
        else:
            space = "  " * (n-2)
            print("* " + space+ "* ")
            