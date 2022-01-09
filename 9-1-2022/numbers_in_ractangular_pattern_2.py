# numbers in Rectangular pattern - 2
# Write a program to print numbers from 1 to M in each column forming a Rectangular
# pattern of M rows and N columns.

def numbers_in_rectangular_pattern(rows,columns):
    print("{0}X{1} Numbers in rectangular pattern".format(rows,columns))
    for i in range(1,rows+1):
        print((str(i)+" ")*columns)
    return

rows = int(input("Enter the number of rows : "))
columns = int(input("Enter the number of columns :"))
numbers_in_rectangular_pattern(rows,columns)
