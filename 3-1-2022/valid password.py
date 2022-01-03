# Valid Passowrd
#consider the password to be valid if it contains at least one digit.

password = input("Please enter the password to valid  :")

is_valid = False

for character in password:
    is_valid = character.isdigit()
    
if is_valid:
    print("Valid Password")
else:
    print("Invalid Password")