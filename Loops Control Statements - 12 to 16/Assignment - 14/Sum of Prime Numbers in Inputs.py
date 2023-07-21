count = int(input())
total = 0
for i in range(count):
    k = int(input())
    fact = 0
    for j in range(1,k):
        if k % j == 0:
            fact += 1 
    if fact == 1:
        total += k 
print(total)




# 5
# 2
# 5
# 6
# 8
# 3
