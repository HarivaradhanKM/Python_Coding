def get_required_words(words, strings):
    result = 0
    for each_word in words:
        for each_string in strings:
            in_same_string = True
            for each_letter in each_word:
                if not each_letter.lower() in each_string:
                    in_same_string = False 
                    break 
            if in_same_string:
                result += 1
                break 
    
    return result
    
def main():
    words = input().split()
    n = int(input())
    
    strings = []
    for i in range(n):
        each_string = input()
        strings.append(each_string)
        
    result = get_required_words(words, strings)
    
    print(result)
        
main()