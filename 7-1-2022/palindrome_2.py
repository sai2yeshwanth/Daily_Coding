def palindrom(word):
    word = word.lower()
    modified_word = ""
    
    for char in word:
        modified_word = char + modified_word
        
    
    if word == modified_word:
        print(True)
    else:
        print(False)
    
    return

word = input("Please the word to check if it's palindrome or not : ")
palindrom(word)