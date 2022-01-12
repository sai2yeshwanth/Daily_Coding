# Create and print List-3
# you are given N numbers as input. Create a list and add the N number which are given as input and print the list.
# the first line of inputis an integer length_of_string
# the next input_items lines each catain an integer.


def create_and_print_list (size_of_string):
    
    creating_new_list = []             # creating New list
    for num in range(size_of_string):   
        input_items = int(input())          # enter the item 
        creating_new_list.append(input_items)  # adding item in to the list
    print(creating_new_list)                    # printing list
    
    return

size_of_string = int(input("Enter the size of the list : "))  #  size of list
create_and_print_list(size_of_string)