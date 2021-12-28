# Given a student has socred M marks in maths, P marks in Physics and C marks in Chemistry.
#Write a program to check if a student is eligible for admission in a professional course. 
#If any one of the below condition is satisfied then the student is eligible
# 1) M >= 70 and P >= 60 and c >= 60
# 2) M + P + C >= 180

maths = int(input())
physics = int(input())
chemistry = int(input())

codition_one = ((maths >= 70) and (physics >=60) and (chemistry >=60))
condition_two = (maths+physics+chemistry >=180)

if condition_two or codition_one:
    print(True)
else:
    print(False)