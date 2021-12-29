# A number is called special Eleven, if it is a multiple of 11 or if it is one more than 
# a multiple of 11. Write a program to check if the given number is a Special Eleven number.

print("Enter the number:")
integer = int(input())

condition_one =  ((integer % 11)==0)
condition_two = ((integer %11)==1)

if condition_one or condition_two :
    print("Special Eleven")
else:
    print("Normal Number")