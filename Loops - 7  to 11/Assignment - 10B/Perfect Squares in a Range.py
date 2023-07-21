A = 9
B = 100

count = 0 
for i in range(A, B+1):
    if int(i ** 0.5) == i ** 0.5:
        count = count + 1 
print(count)