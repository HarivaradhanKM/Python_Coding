n = 5

print("* " * n)

for i in range(1, n-1):
    middle_zeros = "0 " * (n-2)
    row = "* " + middle_zeros + "*"
    print(row)
    
print("* " * n)