# First and last Elements of list.
# you are given an integer N as input. Write a program to read N integers and print a list containing the first and last two inputs.


def first_and_last_elements(size_of_list):
    creating_list = []
    
    for num in range(size_of_list):
        list_item = int(input("Enter the element in the list : "))
        creating_list.append(list_item)
    print("List is {}".format(creating_list))
    if size_of_list >=4:   
        first_and_last_two_elements = creating_list[:2]+creating_list[-2:] # finding first and last two elements with the help of indexing
        print("The first and last two element in the list is {}".format(first_and_last_two_elements))
    else:
        print("You list is size is less than 4 ")
    return

size_of_list = int(input("Enter the size of the list : "))  # Size of the list
first_and_last_elements(size_of_list)