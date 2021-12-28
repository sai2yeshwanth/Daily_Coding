# Given a student has socred M marks in maths, P marks in Physics and C marks in Chemistry.
#Write a program to check if a student is eligible for admission in a professional course based on the following criteria:
# sum of marks is any two subjects >= 100 and M+P+C >= 180

maths = int(input())
physics = int(input())
chemistry = int(input())

condition_one = (maths+physics >= 100) or (maths+chemistry >= 100 ) or (chemistry+physics >=100)
condition_two = maths+physics+chemistry >= 180

if condition_one and condition_two:
    print(True)
else:
    print(False)