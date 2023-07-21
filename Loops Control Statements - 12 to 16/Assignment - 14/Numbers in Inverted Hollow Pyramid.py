n = 3
s = 4
ln = n 
for i in range(1, s+1):
    ln = ln + i
for j in range(1,s+1):
    r = ""
    for k in range(j, s+1):
        if (j == 1) or (j == s-1) or (j==s):
            r = r + str(ln-1) + " "
            ln = ln - 1
        else:
            if k == j or k == s:
                r = r + str(ln - 1) + " "
                ln = ln - 1
            else:
                r = r + "  "
                ln = ln - 1 
    print(("  " * (j-1)) + r)