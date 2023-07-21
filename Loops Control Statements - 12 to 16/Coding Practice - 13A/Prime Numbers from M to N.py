num1 = 5
num2 = 11

for num in range(num1, num2+1):
    fact = 0
    for i in range(2, num):
        if num % i == 0:
            fact = fact +1 
    if fact == 0:
        print(num)