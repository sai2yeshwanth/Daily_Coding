# Write a program to calculate the grade of the student based on marks he/she scored.

marks = float(input("Enter the Markes : "))

grade_A = marks >85                   
grade_B = (marks > 70) 
grade_c = (marks >=60) 

if grade_A:
    print("A")
elif grade_B:
    print("B")
elif grade_c:
    print("C")
else:
    print("F")