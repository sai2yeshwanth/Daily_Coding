# printing message

def message(arg_1, arg_2):
    # using f-string to print a message
    msg = f"{arg_1} is {arg_2} years old."
    return msg
    
name = input("Enter the name : ")
age = int(input("Enter the age : "))
# Call the message function
result = message(arg_1 = name, arg_2 = age)
print(result)