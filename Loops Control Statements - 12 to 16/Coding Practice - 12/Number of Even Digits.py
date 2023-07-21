n = 2563408
Sum = 0
for count in n:
    if int(count) % 2 == 0:
        Sum = Sum + 1
        
if Sum > 2:
    print("Count of even digits is greater than two")
else:
    print("Count of even digits is not greater than two")