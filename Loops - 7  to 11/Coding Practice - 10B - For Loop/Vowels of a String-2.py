N = "india"
count = ""
lenght = 0
Vowels = ("a","e","i","o","u","A","E","I","O","U")
for i in N:
    if i in Vowels:
        count = str(count) + i
        lenght = len(count)
        
if lenght > 2:
    print("String has more than two vowels")
else:
    if lenght <= 2 or lenght == 0:
        print("String doesn't have more than two vowels")