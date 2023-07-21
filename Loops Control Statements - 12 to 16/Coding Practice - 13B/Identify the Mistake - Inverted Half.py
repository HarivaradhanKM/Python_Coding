n = 5

for row_num in range(n, 0, -1):
    row_output = ""
    seq_num = row_num
    while seq_num > 0:
        row_output = row_output + str(seq_num)
        seq_num = seq_num - 1
    print(row_output)