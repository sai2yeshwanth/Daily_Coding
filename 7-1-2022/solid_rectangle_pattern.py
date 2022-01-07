# Solid Rectangle-2
# Write a program to print a rectangle pattern of M rows and N columns using the plus character(+).
# note: Ther is space after each plus (+) character.

M = int(input())            # number of Rows
N = int(input())            # Number of columns

for num in range(1,M+1):        
    print("+ "* N)