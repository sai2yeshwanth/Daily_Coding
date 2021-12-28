# Given a student has socred M marks in maths, P marks in Physics and C marks in Chemistry.
#Write a program to check if a student is eligible for admission in a professional course based on the following criteria:
# sum of marks is any two subjects >= 90 and M>=35, P>=35, C>=35

maths = int(input())
physics = int(input())
chemistry = int(input())

condition_one = (maths+physics >= 90) or (maths+chemistry >=90) or(chemistry+physics >=90)
condition_two = (maths >=35) and(physics>=35) and(chemistry>=35)

if condition_one and condition_two:
    print(True)
else:
    print(False)