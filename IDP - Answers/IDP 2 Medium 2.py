def remove_same_language_words(same_language_words, unique_ancient_words):
    for each_word in same_language_words:
        if each_word in unique_ancient_words:
            unique_ancient_words.remove(each_word)
    
    return unique_ancient_words

def get_same_language_words(same_language_words, unique_ancient_words):
    current_word = same_language_words[0]
    for each_word in unique_ancient_words:
        characters_difference = 0
        for index in range(len(current_word)):
            if each_word[index] != current_word[index]:
                characters_difference += 1
                if characters_difference > 2:
                    break

        if characters_difference == 2:
            same_language_words.append(each_word)
    return same_language_words

def get_number_of_languages(ancient_words):
    unique_ancient_words = set(ancient_words)
    unique_ancient_words = list(unique_ancient_words)
    number_of_languages_with_one_word = 0
    
    same_language_words = []
    same_language_words.append(unique_ancient_words[0])
    contains_only_one_word_in_current_language = True
    
    while True:
        if len(same_language_words) == 0:
            if contains_only_one_word_in_current_language:
                number_of_languages_with_one_word += 1
            if len(unique_ancient_words) == 0:
                return number_of_languages_with_one_word
            same_language_words.append(unique_ancient_words[0])
            contains_only_one_word_in_current_language = True
            
        same_language_words = get_same_language_words(same_language_words, unique_ancient_words)
        
        if len(same_language_words) > 1:
            contains_only_one_word_in_current_language = False
        
        unique_ancient_words = remove_same_language_words(same_language_words, unique_ancient_words)
        same_language_words.pop(0)
        
def main():
    ancient_words = input().split()
    number_of_languages_with_one_word = get_number_of_languages(ancient_words)
    print(number_of_languages_with_one_word)
    
main()