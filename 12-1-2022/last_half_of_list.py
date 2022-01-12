# last half of List
# list contains integer

def last_half_of_string(size_of_list, list_a):
    
    if size_of_list == len(list_a):
        new_list = [] # 

        # coverting string list to integer list
        for num in list_a:
            new_list.append(int(num))

        last_half_list = size_of_list-(size_of_list//2) # finding last half string

        print("Last half of list {}".format(new_list[last_half_list:]))
    else:
        print("Size of list and length of string is different ")
    return

size_of_list = int(input("Enter the siz of list :"))  #size of the list
string = input("Enter the number : ")     #like this 2 3 4 2 1           # list in string format
list_a = string.split()         #converting string to list
last_half_of_string(size_of_list,list_a)