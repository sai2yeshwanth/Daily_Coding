# divisible by seven or not

def divisible_by_seven(arg_1):
    # checking if the given number is divisible by seven or not
    if (arg_1%7 == 0):
        print(f"{arg_1} is divisible by {7}") # using f-string
    else:
        print(f"{arg_1} is not divisible by {7}") # using f-string

n = int(input("Enter the number to check if it's divisible by 7 or not : "))
divisible_by_seven(n)
