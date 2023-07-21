word1 = Manager  #Programmer
word2 = Man      #ammer

word1_len = word1[:3]
word2_len = word2[:3]
match1 = word1_len == word2_len

word1_len_end = word1[-3:]
word2_len_end = word2[-3:]
match2 = word1_len_end == word2_len_end

if match1 or match2:
    print("True")
else:
    print("False")