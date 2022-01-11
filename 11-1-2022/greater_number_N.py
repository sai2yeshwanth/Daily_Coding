# greater than N
# for this problem, the prefilled code will contain a list.your program should create a new list with
# all the elements in existing list the are greater than given number.


def greater_the_N(number):
    num_list = [1, 6, 32, 93, 71, -20, 30, -90, 50]
    # Write your code here
    max_num_list = max(num_list)
    min_num_list = min(num_list)
    
    print("The given list is {}".format(num_list))
    new_list = []
    if number >= min_num_list and number <= max_num_list:
        for num in num_list:
            if num > number:
                new_list += [num]
        print("greater than {0} number in the list is {1} ".format(number,new_list))
    else:
        print("please enter the number between {} to {}".format(min_num_list,max_num_list))
    
    return
number = int(input("Enter the number : "))
greater_the_N(number)