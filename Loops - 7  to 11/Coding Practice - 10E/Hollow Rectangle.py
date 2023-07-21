m = 4
n = 6

print( "* " *n)

for i in range(1, m-1):
    center_spaces = "  " *(n-2)
    row = "* " + center_spaces +  "* "
    print(row)
print( "* " *n)