N = 6
count = 0
for i in range(1, N+1):
    if (N % i == 0) and (N % N == 0):
        count = count+1
    else:
        count = count
if count > 2:
    print("Number has more than 2 factors")
else:
    print("Number doesn't have more than 2 factors")