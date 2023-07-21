N = int(input())

first_Number = int(input())
smallest_Number = first_Number

for i in range(N-1):
    Number = int(input())
    if Number < smallest_Number:
        smallest_Number = Number
print(smallest_Number)