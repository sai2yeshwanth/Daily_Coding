# Given two integer a and b, Write a program to find the greatest among the power of each other
print("Enter the Numbers : ")
A = int(input())
B = int(input())

power_of_AB = A**B
power_of_BA = B**A

condition = power_of_AB >power_of_BA

if condition :
    print(power_of_AB)
else:
    print(power_of_BA)