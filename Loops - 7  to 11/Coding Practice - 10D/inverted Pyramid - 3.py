n = 4

for i in range(0, n):
    if i == 0:
        print(" "*i + ("+ ")*((n+1) - (i+1)))
    else:
        print(" "*i + ("* ")*((n+1) - (i+1)))