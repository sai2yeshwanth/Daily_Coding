# list indexing -2
# for this problem, the perfilled code will contain a list. yYou need to write a program to read N integers, and print the elements at the 
# index location represented by those integers.

def list_index(number):
    programming_languages_list = ["Python", "Java", "Ruby", "C", "C++", "Go", "R", "JavaScript", "Swift", "PHP", "Kotlin", "Perl"]
    # Write your code here
    len_list = len(programming_languages_list)
    for num in range(number):
        index_number = int(input("Enter the Index : "))
        if index_number >= 0 and index_number <= len_list:
            index_value = programming_languages_list[index_number]
            print("You enter the index {0} and output is {1} ".format(index_number,index_value))
        else:
            print("Enter the number between 0 to {}".format(len_list))
    
    return

number = int(input("Enter the no of numbers : "))
list_index(number)