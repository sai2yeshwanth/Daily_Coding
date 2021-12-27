# A company decided to give a bonus of 5% to an employee if his/her years of service is more than five Years.
# Write A program that read a employee salary and years of service and deciedes where the employee gets bonus or not.

print("Enter the Salary of the Employee :")
salary_of_employee = int(input())

print("Enter the Service of the Employee in that Company :")
service_of_employee = int(input())

if service_of_employee >= 5:
    print("Bonus :" , int(salary_of_employee*0.05))
else:
    print("No Bonus") 