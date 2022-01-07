# Swap Case
# given a word, write a program to convert all the uppercase letters to lowercase letters and vice versa

def swap_case(word):
    modified_word = ""

    for char in word:
        uppercase = char.upper()
        if uppercase == char:
            modified_word += char.lower()
        else:
            modified_word += char.upper()
    
    print(modified_word)
    return 

word = input("Enter the word to change the uppercase letter to lowercase letter to uppercase letter : ")
swap_case(word)