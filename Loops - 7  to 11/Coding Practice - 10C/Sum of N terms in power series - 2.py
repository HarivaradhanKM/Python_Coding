x = 3
n = 4

terms = 0
power = 0
for i in range(1, n+1):
    power = power + 2
    term = x ** power 
    terms = terms + term
print(terms)