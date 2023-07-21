N = 11
count = 0
for i in range(1, N+1):
    divisible = True
    for j in range(2, 11):
        if (i % j == 0):
            divisible = False
    if divisible:
        count = count + 1
print(count)