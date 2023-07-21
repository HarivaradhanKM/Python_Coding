n = 6

for i in range(1, n+1):
    stars = "* " * i 
    right_spaces = "  " * (n-i)
    stars1 = "* " * i 
    left_spaces = "  " * (n-i)
    print(stars + right_spaces + left_spaces + stars1)