N = 6
for i in range(2*N-1):
    if i < N:
        leftspace= " " * (N-1-i)
        starts = "* " *(i+1)
        pattern = leftspace + starts
    elif i == (2*N-2):
        leftspace = " " * (N-1)
        pattern = leftspace + "* "
    else:
        leftspace = " " * (i-(N-1))
        hollowspace = "  " *(2*N-3-i)
        pattern = leftspace + "* " + hollowspace + "* "
    print(pattern)
        
