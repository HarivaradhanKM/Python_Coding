X = 10
N = 5

count = 0
a = X + 1
Sum = 1
while count < N:
    while a <= (X + N):
        Sum = Sum * a
        a = a+1
    count = (count + 1)
print(Sum)