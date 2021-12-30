# Write aprogram to print the relation between two number, A and B

first_integer = int(input("Enter the First Number\n"))
second_integer = int(input("Enter the Second Number\n"))

if  first_integer == second_integer :
    print("A == B")
elif first_integer > second_integer:
    print("A > B")
elif first_integer < second_integer:
    print("A < B")
