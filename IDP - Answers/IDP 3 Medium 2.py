def get_string(s, placeholder_values, default_value):
    result = ""
    index = 0
    while index < len(s):
        if s[index] == '(':
            current_index = index + 1
            while current_index < len(s) and s[current_index] != ')':
                current_index += 1
            key = s[index + 1 : current_index]
            
            if key in placeholder_values:
                result += " " + placeholder_values[key] + " "
            else:
                result += " " + default_value + " "
            index = current_index + 1
        else:
            result += s[index]
            index += 1
    
    return result
    
def main():
    s = input()
    n = int(input())
    
    placeholder_values = {}
    for i in range(n):
        key, value = input().split()
        placeholder_values[key] = value 
    
    default_value = input()
    
    result = get_string(s, placeholder_values, default_value)
    
    print(result)
    
main()