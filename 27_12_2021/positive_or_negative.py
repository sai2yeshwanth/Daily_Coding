# Write a Program to find if the given number is Positive or Negative or Zero

print("Enter the Number :")
number = int(input())

if number > 0:
    print("Number is Positive : ",number)
elif number < 0:
    print("Number is Negative : ",number)
else:
    print("Number is Zero : ", number)