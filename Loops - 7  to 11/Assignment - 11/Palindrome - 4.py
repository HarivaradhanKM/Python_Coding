x = No lemon no melon
x = x.lower()
x = x.replace(" ", "")
x = x.replace("'", "")

if (x == x[::-1]):
    print("True")
else: 
    print("False")