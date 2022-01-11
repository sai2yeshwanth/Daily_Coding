#list Concatenation


def list_concatation(n):
    num_list =  [10, 20, 40, 100]
    first_list = [n]+num_list # Add the number in the beginning
    second_list = num_list+[n] # Add the number at the end

    print(first_list)
    print(second_list)
    return
n = int(input("Enter the number to concatenate the list : "))
list_concatation(n)