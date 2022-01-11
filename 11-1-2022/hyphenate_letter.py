# hyphenate letters

def hyphenate_letter(word):
    hyphenate = ""
    len_word = len(word)
    
    for char in range(len_word-1):
        hyphenate += word[char]+"-" 
    
    hyphenate +=word[-1]
    print("Hyphenate lettes of {} is {}".format(word,hyphenate))
    return

word = input("Enter the word : ")
hyphenate_letter(word)