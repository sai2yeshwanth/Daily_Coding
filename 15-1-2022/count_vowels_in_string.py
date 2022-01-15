# count the Vowels

def count_the_vowels(word):
    # initializing count
    count = 0 
    for char in word:
        if (char == "a")or(char == "e")or(char == "i")or(char == "o")or(char == "u"):
            count += 1
        else:
            count += 0
        
    print(f"The vowels in given string '{word}' is '{count}'")
        

word = input("Enter the string : ").lower()
# Call the count_the_vowels function
count_the_vowels(word)
