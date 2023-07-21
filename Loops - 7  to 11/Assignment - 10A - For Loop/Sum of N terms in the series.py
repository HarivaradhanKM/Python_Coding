x = 2
n = 5 

s = 0
k = 1 

for i in range(n):
    s += k * (x**(2*i+1))
    k *= -1
print(s)