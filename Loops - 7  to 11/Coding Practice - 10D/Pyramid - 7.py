n = 5
for i in range(n):
    for j in range(n - i - 1):
        print('', end=' ')
    for k in range(i + 1):
        print(i+1, end=' ')
    print()