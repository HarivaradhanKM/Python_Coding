Num = 6

first_row = "# " * Num
print(first_row)

for i in range(1, Num-1):
    center_spaces_count = (2*Num) - (2 * (i+1)) - 2
    center_spaces = " " * center_spaces_count
    row = "+ " + center_spaces + "+ "
    print(row)

last_row = "+"
print(last_row)