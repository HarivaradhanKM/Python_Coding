word = "theFox"
word_len = len(word)
space = word[0] 
for i in range(1,word_len):
    if (word[i].isupper()):
        space += ""
        space = space + "-" + word[i].lower()
    else:
        space += word[i]
print(space)