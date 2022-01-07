# Valid password
# Write a program to check the given password is valid or not.
#Consider the password to be valid if it consider at lest one uppercase letter, one lowercase letter, one digit

def valid_password(password):
    
    lower_case = not(password == password.lower())   #cheaking lowercase 
    upper_case = not(password == password.upper())   #cheaking uppercase
    
    contains_digit = False                           # Cheaking Digit
    for  character in password:
        is_digit = character.isdigit()
        if is_digit:
            contains_digit = True
    
    case_validation = lower_case and upper_case
    
    if case_validation and contains_digit:
        print("Valid Password")
    else:
        print("Invalid Password")
        
    return

password = input("Please Enter the Password")
valid_password(password)