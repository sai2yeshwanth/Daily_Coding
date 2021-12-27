# Write a program which print the greatest among the three numbers.

print("Enter the First numbers :")
first_number = int(input())

print("Enter the Second number :")
second_number = int(input())

print("Enter the Third number :")
third_number = int(input())

if (first_number >= second_number)and(first_number >= third_number):
    greatest_number = first_number
elif (second_number >= first_number) and (second_number >= third_number):
    greatest_number = second_number
else:
    greatest_number = third_number

print("Greatest Number among there number is : ", greatest_number)