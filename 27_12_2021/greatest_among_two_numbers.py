# Write a program to print the gretest among the two numbers.

print("Enter the First number :")
first_number = int(input())

print("Enter the second number :")
second_number = int(input())

condition = first_number > second_number

if condition:
    print("Greatest Number : ",first_number)
else:
    print("Greatest Number : ",second_number)