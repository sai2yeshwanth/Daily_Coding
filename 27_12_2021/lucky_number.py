# Given two integers, they are considered a lucky pair if any one of them is 6 or
# if their sum or difference is equal to 6

print("Enter the first number :")
first_number  = int(input())

print("Enter the Second number : ")
second_number = int(input())

condition_one = ((first_number or second_number)==6)

condition_two = ((first_number+second_number)==6) 

condition_three = ((first_number-second_number)==6)

if ((condition_one or condition_two)or condition_three):
    print("Luck Number")
else:
    print("Not Luck Number")