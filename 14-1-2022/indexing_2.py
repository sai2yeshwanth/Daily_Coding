# indexng-2
# Write a program that the given function will return the character present at the index N in the word W.
def indexing(arg_1, arg_2):
    # finding the character present at the index in the word
    character = arg_1[arg_2]
    character = f"The character present at the index '{arg_2}' in the word '{arg_1}' is {character}  "   # using f-string

    return character

word = input("Enter the word : ")
index = int(input("Enter the index value : "))
# Call the indexing function
result = indexing(arg_1 = word, arg_2=index)
print(result)