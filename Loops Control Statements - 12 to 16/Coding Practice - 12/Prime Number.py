N = 1

No_of_factors = 0

for i in range(2, N):
    if (N % i ==0):
        No_of_factors = No_of_factors + 1
if No_of_factors == 0:
    print("Prime Number")
else:
    print("Not a Prime Number")