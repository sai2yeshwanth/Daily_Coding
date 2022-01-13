# Average of Given Numbers

def average_of_given_number(list_a):
    
    new_list = []
    for i in list_a:
        new_list.append(int(i))
        
    new_list = round((sum(new_list)/len(new_list)),2)
    
    
    return new_list

list_a = input("Enter the number : ").split()
result = average_of_given_number(list_a)
print("Average of given number \n{}".format(result))