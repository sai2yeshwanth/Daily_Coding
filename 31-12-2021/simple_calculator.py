# Write a program to creat a mean driven calculator the peforms basic arithmetic operations(+,-,*,/, and %)

arithmetic_operator = input("Enter the Arithmetic operator \n")
first_integer = int(input("Enter the first_number \n"))
second_integer = int(input("Enter theSecond_number \n"))

if arithmetic_operator == "+":
    print("You select addition :",first_integer + second_integer)
elif arithmetic_operator == "-":
    print("You select subscription",first_integer - second_integer)
elif arithmetic_operator == "*":
    print("You select Multiplication",first_integer * second_integer)
elif arithmetic_operator =="/":
    print("You Select Division",first_integer / second_integer)
elif arithmetic_operator == "%":
    print("You select Modulus",first_integer %second_integer)
else:
    print("Please Enter the valid Arithmetic_operator")