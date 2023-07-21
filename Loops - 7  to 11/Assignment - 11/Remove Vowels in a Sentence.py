N = "Hello World"

Vowels = ("a","e","i","o","u","A","E","I","O","U")
for i in N:
    if i in Vowels:
        N = N.replace(i,"")
print(N)