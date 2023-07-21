def convert_string_to_integers(n, numbers):
    for index in range(n):
        numbers[index] = int(numbers[index])
        
    return numbers

def get_right_left_differences(n, numbers):
    left_sum = []
    right_sum = []

    for index in range(n):
        left_sum.append(sum(numbers[:index]))
        right_sum.append(sum(numbers[index + 1:]))

    difference = []

    for index in range(n):
        difference.append(str(right_sum[index] - left_sum[index]))

    return difference
    
def main():
    numbers = input().split()
    n = len(numbers)
    
    numbers = convert_string_to_integers(n, numbers)
        
    difference = get_right_left_differences(n, numbers)

    difference = " ".join(difference)
    
    print(difference)
    
main()