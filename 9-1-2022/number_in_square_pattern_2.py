# numbers in a square pattern - 2
# write a program to print number from 1 to n in each column forming a square pattern of N rows and N columns

def numbers_in_square_pattern(number):
    print("{} in square pattern ".format(number))
    for num in range(1,number+1):
        print((str(num)+" ")*number)
    return

number = int(input("Enter the Number to print in square pattern : "))
numbers_in_square_pattern(number)