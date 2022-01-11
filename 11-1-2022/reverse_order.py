# Reverse order 
# Given an Integer N, Write a program to print the given N inputs in the reverse order.

def reverse_order(length_of_list):
    print("createing a list in reverse order inputs ")
    reverse_order = []
    for num in range(length_of_list):
        input_list = input("Enter the item in the list : ")
        reverse_order = [input_list]+reverse_order
        print(reverse_order)
    for char in reverse_order:
        print(char)
    
    return

length_of_list = int(input("Enter the lenght of list : "))
reverse_order(length_of_list)