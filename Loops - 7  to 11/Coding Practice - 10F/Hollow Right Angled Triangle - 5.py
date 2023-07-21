N = 5

for i in range(0, N):
    if i == 0:
        print("  " * (N-1) + "*")
    elif i == N-1:
        print("* " * N)
    else:
        left_space = "  " * (N-i-1)
        hollow_space = ("  " * (i -1))
        print(left_space + "* " + hollow_space + "*")