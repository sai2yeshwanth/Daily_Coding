# Write a program to find the hypotensuse H od a right-angled tringle of size A and B

import math

print("Enter Number")
A = int(input())
B = int(input())

condition = (A**2)+(B**2)

print("hypotenuse :",int(math.sqrt(condition)))