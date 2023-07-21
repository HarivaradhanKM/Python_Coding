m = 6
n = 23

count = 0
Num_divisible_6 = ""

for Num in range(m, n+1):
    if Num % 6 == 0:
        count = count + 1
        Num_divisible_6 = Num_divisible_6 + str(Num) + " "
        
if count == 0:
    print("No Numbers Found")
else:
    print(Num_divisible_6)