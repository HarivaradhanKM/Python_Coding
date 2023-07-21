n = 5
for i in range(1, n+1):
    spaces = "  " * (n-i)
    plus = "+ " * (i-1) + "#"
    print(spaces+plus)

for i in range(1, n):
    spaces= "  " * i 
    plus = "+ " * (n-i-1) + "#"
    print(spaces+plus)