# list Concatenation -2
# write a program to read N inputs and print a list containing the first and last three inputs

def list_concatenation(length_of_list):
    
    if length_of_list >= 6:
        print("Creating a list :")
        creating_list = []
        for num in range(length_of_list):
            input_list = input("Enter the item into the list :")
            creating_list += [input_list]

        print("print the first three and last three in the list ")    
        new_list = creating_list[:3]+creating_list[length_of_list-3:]
            
        print(new_list)
    else:
        print("Please enter the length of the string minimum 6 ")
    return

length_of_list = int(input("Enter the length of the list : "))
list_concatenation(length_of_list)