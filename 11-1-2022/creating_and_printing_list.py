# creating and print list-2
# write a program to print a list with the given N input

def create_and_print_list(number):
    print("Creating a list ")
    creating_new_list = []
    for num in range(number):
        input_list = input("Enter the item to the list : ")
        creating_new_list += [input_list]
    print("Printing a list ")
    print(creating_new_list)
    
    return

number = int(input("Enter the length of the list : "))
create_and_print_list(number)