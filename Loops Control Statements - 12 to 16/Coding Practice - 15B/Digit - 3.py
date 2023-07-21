n = 5
r = 2*n-1
for i in range(1, (r)+1):
        if (i == 1) or (i == n) or (i == r):
            star = "* " * n
            print(star)
        else:
            space = "  " * (n-2)
            print("  " + space + "*")