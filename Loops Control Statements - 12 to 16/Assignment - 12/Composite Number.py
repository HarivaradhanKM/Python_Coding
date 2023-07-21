N = 12
Sum = 0
for i in range(1, N+1):
    if (N % i == 0) and (N % N == 0):
        Sum = Sum + 1
if Sum > 2:
    print("True")
else:
    print("False")