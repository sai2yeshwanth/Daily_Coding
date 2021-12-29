# Write a program to print the relation between two numnbers, X and Y

first_number = int(input())
second_number = int(input())

condition = first_number < second_number

if condition:
    print("X < Y")
else:
    print("X >= Y")