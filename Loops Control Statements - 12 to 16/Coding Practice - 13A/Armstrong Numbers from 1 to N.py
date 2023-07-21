n = 200
for i in range(1, n+1):
    Sum_of_power = 0
    i = str(i)
    power = len(i)
    for digit in i:
        digit = int(digit)
        Sum_of_power  = Sum_of_power + digit ** power
    i  = int(i)
    is_armstrong = Sum_of_power == i 
    if is_armstrong:
        print(i)