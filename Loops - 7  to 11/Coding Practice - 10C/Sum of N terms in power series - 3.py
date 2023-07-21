x = 2
n = 6
Sum = 0
power = 0

for i in range(1, n+1):
    power = power +2
    term = x ** power
    nagative = (i % 2 == 0)
    if nagative:
        term = term * (-1)
    Sum = Sum + term
print(Sum)