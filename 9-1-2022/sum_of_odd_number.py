# sum of odd numbers
# write a program to find the sum of odd number in first N natural numbers


def sum_of_odd_numbers(number):
    odd = 0 
    for num in range(1,number+1):
        if not(num%2) == 0:
            odd+=num

    print("sum of odd numbers is {}".format(odd)) 
    
    return

number = int(input("Enter the number : "))
sum_of_odd_numbers(number)