# Product of the Given Numbers
# Given an integer N, Write a program which reads N inputs and prints the product of the given input integers.

def product_of_the_given_number(N):
    product = 1

    for num in range(1,N+1):
        number = int(input("Enter the {} Number : ".format(num)))  #input
        product *=  number      #muliplying the each input with product

    print("The product of the given number's :",product)
    return



N = int(input("Enter the number to Read the number of inputs : "))        # to read the number  of inputs
product_of_the_given_number(N)