# Shuffle String
# given a string and N integers, where N is the length of the string,
# write a program to print the string after shffling the characters as per the order of the integers given.

def shulffle_string(word):
    
    length_of_word = len(word)
    modified_word = ""
    
    for i in range(length_of_word):
        index_number = int(input("Enter the Index number : "))
        modified_word +=word[index_number]
    
    print("Modified Word of {} is {} ".format(word,modified_word))
    return

word = input("Enter the Shuffle Word : ")
shulffle_string(word)