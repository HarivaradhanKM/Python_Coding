N = 12
Count=0;
for i in range(1, N+1):
    if((i % 2 == 0) and (i % 3 == 0)):
        Count=Count+1
print (Count)