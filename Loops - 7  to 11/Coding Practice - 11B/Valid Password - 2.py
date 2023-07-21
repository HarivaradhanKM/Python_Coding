S = "Qwerty123"
is_upper = False
for i in S:
    if (i.isupper()) == True:
        is_upper = True
if is_upper == True:
    print("Valid Password")
else:
    print("Invalid Password")