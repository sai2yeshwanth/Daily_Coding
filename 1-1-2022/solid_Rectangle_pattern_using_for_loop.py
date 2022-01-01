# write a program to print a solid rectangle pattern of M number of rows and N numbers of Columns using Asterisk character(*)
#using for-loop

M = int(input("Please enter the M rows : "))
N = int(input("Please enter the N column : "))

for i in range(1,M+1):
    print("* "*N)