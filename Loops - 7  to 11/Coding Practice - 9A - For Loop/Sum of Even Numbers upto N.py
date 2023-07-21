N = 6
Even = 1
Sum = 0
while Even <= N :
    if(Even % 2 == 0):
        Sum = Sum + Even
    else:
        Sum = Sum
    Even = Even + 1
print(Sum)