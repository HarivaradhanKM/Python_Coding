n = 1030800
Sum = 0
for count in n:
    if int(count) == 0:
        Sum = Sum + 1
if Sum > 3:
    print("Count of zeroes is greater than three")
else:
    print("Count of zeroes is not greater than three")