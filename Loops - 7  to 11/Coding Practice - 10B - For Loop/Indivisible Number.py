N = 15
output=""
for i in range(2, 9+1):
    find = (N % i == 0)
    if find == True:
        output = find
if output:
    print("Divisible Number")
else:
    print("Indivisible Number")