# special number to read a single line of input, which is two-digit integer and
# print "Special Number" if any one of the followeing conditions are satisified
# 1. the sum of the digit is 7
# 2. one of the digits is 7
# 3. the number is a multiple of 7
# print "Normal Number" is all other cases.

print("Enter the two-digite integer number:")
num = input()

first_digit = int(num[0])
second_digit = int(num[1])
num = int(num)

condition_one =  (first_digit+second_digit == 7)
condition_two = (first_digit==7) or (second_digit==7)
condition_three = (num%7)==0

if condition_one or condition_two or condition_three:
    print("Special Number")
else:
    print("Normal Number")
