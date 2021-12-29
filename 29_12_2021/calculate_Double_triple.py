# write a program to print the triple of the number N if is multiple of 3 otherwise, double of N.

print("Enter the Number :")
N = int(input())

condation = (N%3)==0

if condation:
    print("Number Triple :",N*3)
else:
    print("Number Double:",N*2)