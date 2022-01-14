# Number of lowercase and uppercase letter in a word

def count_of_lowercase_and_uppercase_letters(arg_1):
    # initializing count_of_uppcase
    count_of_uppercase = 0
    # initializing count_of_lowercase = 0
    count_of_lowercase = 0
    # initializing uppercase 
    uppercase = arg_1.upper()  
    
   
    for i in range(len(arg_1)):
        if arg_1[i] == uppercase[i]:
            count_of_uppercase+=1
        else:
            count_of_lowercase+=1
    
    
    print(f"The number of uppercase character in the word '{arg_1}' is '{count_of_uppercase}'")
    print(f"The number of lowercase character in the word '{arg_1}' is '{count_of_lowercase}'")


word = input("Enter the word : ")
# Call the count_of_lowercase_and_uppercase_letters function
count_of_lowercase_and_uppercase_letters(arg_1=word)