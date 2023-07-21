N = 50
Count=0;
for i in range(1, N+1):
    if((i%6==0) and (i%8 ==0)):
        Count=Count+1
print (Count)