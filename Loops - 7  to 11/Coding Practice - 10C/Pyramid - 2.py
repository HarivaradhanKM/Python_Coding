size = int(input())

for i in range(size):
    # print spaces
    for j in range(size-i-1):
        print(" ", end=" ")
    for k in range(2 * i+1):
        print(i+1, end=" ")
    print()