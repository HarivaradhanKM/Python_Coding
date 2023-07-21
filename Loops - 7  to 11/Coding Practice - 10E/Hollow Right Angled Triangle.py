n = 5

print("* ")

for i in range(1, n-1):
    center_space = " " * (2* (i-1))
    row = "* " + center_space + "* "
    print(row)

print("* " * n)
    