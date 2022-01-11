# list indexing
# for this problem, the perfilled code will contain a list. write a program to print the element at the given index location 

def list_indexing(index_number):
    color_list = ["Red", "Orange", "Yellow", "Pink", "Green", "Blue", "Purple", "Black", "White"]
    # Write your code here
    print("Color List is {}".format(color_list))
    if index_number >=0 and index_number <=8:
        print("you enter index number is {0} and color is {1}".format(index_number,color_list[index_number]))
    else:
        print("please enter the number betweem 0 to 8 ")
    return

index_number = int(input("Enter the index number to print the color (0 to 8) : "))
list_indexing(index_number)