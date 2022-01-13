# Largest Number In list

def smallest_number_in_list(list_x):
    # initializing new_list
    new_list =[]
    for i in list_x:
        new_list.append(int(i))
    
    return min(new_list) # using min() we can find smallest number in a list

list_a = input().split(",")
result = smallest_number_in_list(list_a)
print(result)