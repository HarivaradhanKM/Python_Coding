N = 10
count=0
for a in range(1,N-1):
    for b in range(a+1,N):
        for c in range(b+1,N+1):
            if (a+b+c == N):
                count+=1
print(count)