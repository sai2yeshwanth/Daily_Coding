# list indexing -3
# Given N number, and an index, write a program to store the numbers in a list and print the number at the given index.
# For this problem, each input will contain T test cases. Each test case will given an index Ki as input, which should 
# be considered to print the number.

# The first line of input is an integer N.
# The second line of input is an integer T represting the number of test cases.
# The next N lines contain integers representing the numbers of the list.
# The next T lines contain integer Ki for each line.

def list_indexing(size_of_list,test_cases):
    
    creating_list = []
    for num in range(size_of_list):
        intput_item = int(input("Enter the item in to list : "))
        creating_list.append(intput_item)
    print(creating_list)   # creating list 
        
    for num in range(test_cases):
        
        index = int(input("index value"))
        if len(creating_list) > index: 
            print(creating_list[index])   
        else:
            print("please enter the index betwwen 0 to {}".format(len(creating_list)))
    
    return

size_of_list = int(input("Enter the size of list : "))  #size of list
test_cases = int(input("Enter the test case : "))  #test_cases
list_indexing(size_of_list,test_cases)
