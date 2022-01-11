
# List Repetition
# given two integers M and N, write a program to create a list with element M repeated bt N time.
# the first line of input will be integer.
# the second line of input will be positive integer.

def list_repetiton(number,repeated_number):
    
    if repeated_number > 0:
        output = [number]* repeated_number
        print("You enter the number {0} and it's repeated by {1} times and list is {2}".format(number,repeated_number,output))
    else:
        print("Please enter the positive Repeated Number")
    
    return

number = int(input("Enter the number : "))
repeated_number = int(input("Enter the number to how many time is repeated : "))

list_repetiton(number,repeated_number)