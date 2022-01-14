# Second character in the word

def second_character(arg_1):
    # using indexing to find out the second character of word
    output = arg_1[1]
    output = f"The second character of the {arg_1} is '{output}'" # using f-string
    return output
    
    
word = input("Enter the word : ")
# Call the second_character function
result = second_character(arg_1 = word)
print(result)