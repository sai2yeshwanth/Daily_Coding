# write a program to print a solid rectangle pattern of M number of rows and N numbers of Columns using Asterisk character(*)

M = int(input("Please Enter the M row : "))
N = int(input("Please Enter the N column : "))

counter = 1
while counter <= M:
    print("* " * N)
    counter +=1