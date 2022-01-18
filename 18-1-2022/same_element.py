# Same Elements
# write a program to check if all the elements in given list are same.


def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        new_list.append(int(item))
    return new_list

num_list = input("Enter the numbers ").split()
num_list = convert_string_to_int(num_list)

num_set = set(num_list)
if len(num_set)==1:
    print(True)
else:
    num_list = list(num_set)
    num_list.sort()
    print(num_list)