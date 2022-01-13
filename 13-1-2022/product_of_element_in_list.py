# product of elements in the list

def product_of_element_in_the_list(list_a):
    
    product = 1
    for num in list_a:
        product *= int(num)
    
    
    return product

list_a = input("Enter the number ").split()
result = product_of_element_in_the_list(list_a)
print("Product of element in list \n"+str(result))