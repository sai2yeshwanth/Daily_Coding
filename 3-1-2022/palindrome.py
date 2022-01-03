# palindrome
# palindrome means if any word is equal to reverse of that word

string = input("Enter the Word to cheak if it's palindrome or not \n").lower()

reverse_string = ""

for char in string:
    reverse_string = char+reverse_string

if string == reverse_string:
    print("It's a Palindrome")
else:
    print("It's not a Palindrome")