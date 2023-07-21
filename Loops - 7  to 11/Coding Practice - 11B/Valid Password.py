S = "Qwerty123"
is_digit = False
for i in S:
    if (i.isdigit()) == True:
        is_digit = True
if is_digit == True:
    print("Valid Password")
else:
    print("Invalid Password")