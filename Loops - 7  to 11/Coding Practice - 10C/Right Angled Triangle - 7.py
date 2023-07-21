rows  = 5

for each_number in range(1, rows +1):
    spaces = " " * (rows - each_number)
    is_last_row = (each_number == rows)
    if is_last_row:
        hashes = "#" * each_number
        print(spaces + hashes)
    else:
        star = "*" * each_number
        print(spaces + star)