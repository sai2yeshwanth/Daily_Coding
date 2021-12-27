# Write a progrom to check if the give two digit number is greater than 25 and its first digit is greater than its second digit

number = input()

first_digit =  int(number[0])
second_digit = int(number[1])

number_is_greater_than_25 = int(number) > 25

first_second_digit = first_digit > second_digit

#print(number_is_greater_than_25)
#print(first_second_digit)

comparing_two_condition = number_is_greater_than_25 and first_second_digit
print(comparing_two_condition)