N1 = int(input())
N2 = int(input())
count = 0
for i in range(N1, N2+1):
    count = count+len(str(i))
print(count)