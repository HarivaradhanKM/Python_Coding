def get_maximum_number_of_children(money, children):
    if money < children:
        return -1
    distribution = [1]*children
    money -= children
    index = 0
    while money > 0 and index < children:
        while distribution[index] != 8 and money > 0:
            if distribution[index] == 3 and money <= 1:
                break
            distribution[index] += 1
            money -= 1
        index += 1
    
    number_of_children = distribution.count(8)
    
    if money > 0:
        number_of_children -= 1
        
    if number_of_children == -1:
        return -1
    else:
        return children - number_of_children

def main():
    money = int(input())
    children = int(input())
    
    number_of_children = get_maximum_number_of_children(money, children)
    
    print(number_of_children)
    
main()