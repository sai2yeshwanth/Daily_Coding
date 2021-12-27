# Given three angles of a triangle, write a program to check whether the tringle is valid or not. 
# A triangle is valid if the sum of its three angles is equal to 180 degrees.


print("Enter the first angle of the triangle : ")
first_angle = int(input())

print("Enter the second angle of the triangle :")
second_angle = int(input())

print("Enter the Third angle of the triangle :")
third_angle = int(input())

condition = (first_angle+second_angle+third_angle == 180)

if condition :
    print("Its an Triangle")
else:
    print("Not An Triangle")


