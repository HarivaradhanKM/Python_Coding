num1 = 3
num2 = 7
sum = 0
for num in range(num1, num2+1):
    fact = 0
    for i in range(2, num):
        if num % i == 0:
            fact = fact + 1
    if fact == 0:
        sum = sum + num
print(sum)