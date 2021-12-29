# Given a two-digit number, print "Lucky Number" if any of the following conditions are satisfied.
# 1. The number is a multiple of 9
# 2. One of the digits is 9
# print "Unlucky Number" in all other cases.

print("Enter the Number : ")
number = input()

first_digit = int(number[0])
second_digit = int(number[1])
number = int(number)

if  (number%9)==0:
    print("Lucky Number")
elif (first_digit==9)or(second_digit==9):
    print("Lucky Number")
else:
    print("Unlucky Number")