# sum of digits 
# write a program to print the sum of all the digits in the given number.

number = input("enter the numbers : ")      #like this 5641455

sum_of_digits = 0

for digit in number:
    sum_of_digits += int(digit)

print("Sum of digits :",sum_of_digits)