N = 10
K = 1 

count = 0
while (10 ** K) <= N:
    count += 9 * 10 ** (K-1) * K 
    K +=1 
count += (N - 10 ** (K-1) + 1) * K
print(count)