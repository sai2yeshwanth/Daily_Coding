# Largest Number in the list 

def largest_number_in_the_list(list_a):
    
    new_list = []
    for i in list_a:
        new_list.append(int(i))
    
    largest_number = new_list[0]
    
    for i in new_list:
        if i > largest_number:
            largest_number= i
    
    return largest_number

list_a = input("Enter the number :").split()
result = largest_number_in_the_list(list_a)
print("The largest number in a list is {}".format(result))