# Given a student has socred M marks in maths, P marks in Physics and C marks in Chemistry.
# Write a program to check if a student is eligible for admission in a professional course. if any one of the below condition is satisifed them the student is eligible:
# 1)M>=60,P>=50,C>=45 and M+P+C>=180
# 2) Total in M and P>=120 or Total in C and P>=110

maths = int(input())
physics = int(input())
chemistry = int(input())

condition_one = ((maths >= 60)and(physics >= 50)and(chemistry >= 45) and (maths+physics+chemistry >= 180))
condition_two = ((maths+physics>=120)or(chemistry+physics >=110))

if condition_one or condition_two:
    print(True)
else:
    print(False)