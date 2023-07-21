def convert_string_to_integers(given_list):
    for index in range(len(given_list)):
        given_list[index] = int(given_list[index])
    return given_list

def convert_integers_to_string(given_list):
    for index in range(len(given_list)):
        given_list[index] = str(given_list[index])
    return given_list

def get_new_powerstatus(customers, powerstatus, n):
    max_customers_served = 0
    num_of_hours = len(powerstatus)
    new_powerstatus = []
    
    for index in range(num_of_hours - n + 1):
        backup_used = [1]*n
        current_powerstatus = powerstatus[:index] + backup_used + powerstatus[index + n:]
        
        served_customers = 0
        for each_hour in range(num_of_hours):
            if current_powerstatus[each_hour] == 1:
                served_customers += customers[each_hour]
                
        if served_customers > max_customers_served:
            max_customers_served = served_customers
            new_powerstatus = current_powerstatus
    
    return new_powerstatus
    
def main():
    customers = input().split()
    powerstatus = input().split()
    n = int(input())
    
    customers = convert_string_to_integers(customers)
    powerstatus = convert_string_to_integers(powerstatus)
        
    new_powerstatus = get_new_powerstatus(customers, powerstatus, n)

    new_powerstatus = convert_integers_to_string(new_powerstatus)

    new_powerstatus = " ".join(new_powerstatus)
    
    print(new_powerstatus)
    
main()