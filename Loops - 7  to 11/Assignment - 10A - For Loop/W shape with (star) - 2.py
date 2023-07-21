n = 5
print("* " * (2*n-1))
for i in range(1,n):
    print(" " * i, end="")
    print("* " *(n-i), end="")
    print("  " *(i-1), end="")
    print("* " *(n-i), end="")
    print()