# Striped Rectangle
# Given an integer number M,N as input. write a program to print a striped Rectangular pattern of
# M rows and N columns using (+ and - ) character

def stript_rectangle(M,N):
    
    print("{0}X{1} striped rectangular pattern".format(M,N))

    even_rows = "- "*N
    odd_rows = "+ "*N
    for i in range(1,M+1):
        if (i%2)==0:
            print(even_rows)
        else:
            print(odd_rows)
    
    return
M = int(input("Enter the number of Rows : "))
N = int(input("Enter the Number of Columns : "))
stript_rectangle(M,N)