m = 4
n = 8

print("* " * n)

for i in range(1, m-1):
    center_zeros = "0 " * (n-2)
    row = "* " + center_zeros + "*"
    print(row)

print("* " * n)