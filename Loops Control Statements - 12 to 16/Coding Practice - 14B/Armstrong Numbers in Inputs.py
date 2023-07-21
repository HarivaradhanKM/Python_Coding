n = int(input());
a = [];
for i in range(n):
    a.append(int(input())) 
for x in range(n):
    Sum_of_power = 0
    i = str(a[x])
    power = len(i)
    for digit in i:
        digit = int(digit)
        Sum_of_power  = Sum_of_power + digit ** power
    i  = int(i)
    is_armstrong = Sum_of_power == i 
    if is_armstrong:
        print(i)
        
        
        
        
# 4
# 8
# 27
# 153
# 374
