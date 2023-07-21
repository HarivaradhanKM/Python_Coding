a = "Python"
len_of_a = len(a)
b = ""
for i in range(len_of_a):
    if i < len_of_a - 1:
       b = (b + a[i] + "-")
    else:
        b = (b + a[i])
print(b)
     