# Givem an integer between 0 to 10000, write a program to print the sum of digits.

number = input("Enter the number between 0 to 10000 :")

first_condation = (len(number) == 1) 
second_condition = (len(number) == 2)
third_condition = (len(number) == 3)
fourth_condition = (len(number) == 4) 

if first_condation:
    print(number)
elif second_condition:
    first = int(number[0])
    second = int(number[1])
    print(first+second)
elif third_condition:
    first =int(number[0])
    second = int(number[1])
    third = int(number[2])
    print(first + second +third)
elif fourth_condition:
    first =int(number[0])
    second = int(number[1])
    third = int(number[2])
    fourth = int(number[3])
    print(first + second + third + fourth)
else:
    print("Please enter the number between 0 to 10000")