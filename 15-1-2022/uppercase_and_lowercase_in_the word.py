# uppercase and lowercase letters
def get_lower_and_upper_case_letters(word):
    # initializing upper and lower
    upper = ""
    lower = ""
    for char in word:
        if char.isupper():
            upper += char
        else:
            lower += char
        
    print(f"The upper characters in the word '{word}' is '{upper}'")
    print(f"The lower characters in the word '{word}' is '{lower}'")
    

word = input("Enter the word : ")
# Call the get_lower_and_upper_case_letters function
get_lower_and_upper_case_letters(word)