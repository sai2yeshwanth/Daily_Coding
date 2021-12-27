# write a program that reads a single line of input and prints that first
# and last character of the given input and priints the asterisk character(*)
# in place of remaining characters.


print("Enter the Word :" )
string = input()

length_of_string = len(string)
#print(length_of_string)

first_character_of_string = string[0] #finding the first character of the string  
last_character_of_string = string[-1] #finding the last character of the string

#print(first_character_of_string)
#print(last_character_of_string)

length_masking = len(string)-2 
masking = "*"*length_masking   
#print(masking)

print(first_character_of_string + masking + last_character_of_string)
