num1 = 3
num2 = 15
output = ""
for num in range(num1, num2+1):
    if num > 1:
        fact = 0
    else:
        fact = 1
    for i in range(2, num):
        if num % i == 0 :
            fact += 1
    if fact == 0:
        output = output + str(num) + " "
if len(output) >=1:
    print(output)
else:
    print("No Prime Numbers Found")
            