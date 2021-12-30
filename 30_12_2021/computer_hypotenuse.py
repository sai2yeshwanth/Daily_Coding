# Write a program to find the hypotensuse H od a right-angled tringle of size A and B

import math

A = int(input("Enter the Size A : "))
B = int(input("Enter The Size B : "))

condition = (A**2)+(B**2)

print("Hypotenuse :",int(math.sqrt(condition)))