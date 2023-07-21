S = "Qwerty123"

lower = 0
upper = 0
digit = 0
special = 0
for i in S:
    if (i.islower()):
        lower+=1
    if (i.isupper()):
        upper+=1
    if (i.isdigit()):
        digit+=1
    if (i == "@" or i == "-"):
        special+=1
if (lower>=1 and upper>=1 and digit>=1 or special>=1 and upper+lower+digit+special==len(S)):
    print("Valid Password")
else:
    print("Invalid Password")