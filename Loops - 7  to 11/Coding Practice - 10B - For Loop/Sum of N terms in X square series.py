X = 4
N = 3

Sum = 0
for i in range (1, N+1):
    Num = eval(str(X) * i)
    Num = Num ** 2
    Sum += Num
print(Sum)