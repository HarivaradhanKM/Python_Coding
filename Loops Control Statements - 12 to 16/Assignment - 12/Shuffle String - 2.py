word1 = bring
word2 = camel

new_word = ""

for i in range (len(word1)):
    if (i % 2 == 0):
        new_word = new_word + word1[i]
    else:
        new_word = new_word + word2[i]
        
print(new_word)