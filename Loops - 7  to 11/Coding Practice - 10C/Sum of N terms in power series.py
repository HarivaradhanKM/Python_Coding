x = 2
n = 6

terms = 0
power = 1 

for i in range(1, n+1):
    term = x ** power
    power = power + 2
    terms = terms + term
    
print(terms)