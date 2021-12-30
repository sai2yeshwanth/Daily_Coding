# Write a program to check if a given 3-digit number X is an Armstrong number or not.

number = input("Enter the three Digit Number : ")

first_digit = int(number[0])
second_digit = int(number[1])
third_digit = int(number[2])

number = int(number)
codition = (number ==((first_digit**3)+(second_digit**3)+(third_digit**3)))

print(codition)