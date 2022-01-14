# Add two Number
def add(arg_1, arg_2):
    # Adding a and b
    adding = arg_1+arg_2
    adding = f"{arg_1} + {arg_2} = {adding}" #using f-string
    return adding
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
# Call the add function
result = add(arg_1 = a,arg_2 = b)
print(result)