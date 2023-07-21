M = 150
N = 200
output = ""
for i in range(M, N+1):
    lenght = len(str(i))
    i = str(i)
    Sum_of_power = 0
    count = 0
    while count < lenght:
        Sum_of_power  = Sum_of_power + (int(i[count])) ** lenght
        count += 1
    if Sum_of_power == int(i):
        output = output + str(Sum_of_power) + " "
if output == "":
    print("-1")
else:
    print(output)