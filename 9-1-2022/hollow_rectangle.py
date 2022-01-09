# Hollow Rectangle
# Given two integers M and N, Write a program to print a hollow number rectangle pattern of
# M rows and N columns using the asterisk character(*)

def hollow_rectangle(rows,columns):

    print("{0} X {1} Hollow Rectangle is below".format(rows,columns))

    print("* "*columns)
    
    for i in range(rows-2):
        print("* "+("  "*(columns-2))+"* ")
    
    print("* "* columns)
    return

M = int(input("Enter the Number of Rows : "))
N = int(input("Enter the Number of Columns : "))

hollow_rectangle(M,N)