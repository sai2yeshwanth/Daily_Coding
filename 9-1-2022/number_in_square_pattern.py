# Numbers is square pattern 
# Write a program to print numbers from 1 to N in each row forming a square pattern of N rows and N columns.

def number_in_square_pattern(number):

    print("{0} in square pattern : ".format(number))

    num_string = ""
    for num_column in range(1,number+1):
        num_string += str(num_column)+" "
        
    for num in range(number):
        print(num_string)
        
    return

number = int(input("Enter the number to print a numbers in square pattern : " ))
number_in_square_pattern(number)