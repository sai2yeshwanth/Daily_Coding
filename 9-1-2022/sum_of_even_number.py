# Sum of Even Numbers
# Write a program to find the sum of even numbers in first N natural numbers.

def sum_of_even_number(number):
    
    sum_of_even = 0
    
    for i in range(1,number+1):
        if (i % 2) == 0:
            sum_of_even += i
    
    print("sum of the even number from 1 to {0} is {1}".format(number,sum_of_even))
    return

number = int(input("Enter the number to sum the N natural number :"))
sum_of_even_number(number)