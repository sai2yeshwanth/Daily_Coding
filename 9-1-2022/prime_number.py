# Prime Number
# Write a program to check the given number is prime or not

def prime_number(number):
    
    if number > 1:
        counter = 0
    else:
        counter = 1

    for num in range(2,number):
        if (number % num) == 0:
            counter += 1
    
    if counter == 0:
        print("{0} is a Prime Number".format(number))
    else:
        print("{0} is a not prime Number".format(number))

    return

number = int(input("Enter the number to check if it's prime or not : "))
prime_number(number)