# palindrome
# palindrome means word or sentence reads the same backwards or forwards

string = input("Enter the Word to cheak if it's palindrome or not \n").lower()

reverse_string = ""

for char in string:
    reverse_string = char+reverse_string

if string == reverse_string:
    print("It's a Palindrome")
else:
    print("It's not a Palindrome")