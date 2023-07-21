rows = 4
for i in range(rows):
    count = 0
    for k in range(rows-i-1):
        print(end="  ")
    for j in range(i+1):
        count = count + 1 
    num = count
    for j in range(i+1):
        print(num, end=" ")
        num = num-1
    print()