# Sum of list elements
# Given a list of numbers, write a program to print the sum of the number in the list


def sum_of_list_element(numbers):
    
    sum_of_list = 0
    for num in numbers:
        sum_of_list +=int(num)
    print("sum of elements in list is {}".format(sum_of_list))
    return 

numbers = input("Enter the number : ").split()
sum_of_list_element(numbers)