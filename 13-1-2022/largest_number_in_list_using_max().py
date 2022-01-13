# Largest Number In list

def lagerst_number_in_list(list_x):
    # initializing new_list
    new_list =[]
    for i in list_x:
        new_list.append(int(i))
    
    return max(new_list) # using max() we can find largest number in a list

list_a = input().split(",")
result = lagerst_number_in_list(list_a)
print(result)