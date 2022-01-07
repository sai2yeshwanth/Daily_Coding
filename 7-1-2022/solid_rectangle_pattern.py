# Solid Rectangle-2
# Write a program to print a rectangle pattern of M rows and N columns using the plus character(+).
# note: Ther is space after each plus (+) character.

def Solid_tringle_pattern_plus(M,N):
    
    for num in range(M):
        print("+ "*N)

    return
    

M = int(input("Enter the Number of Rows : "))            # number of Rows
N = int(input("Enter the Number of Columns : "))            # Number of columns

Solid_tringle_pattern_plus(M, N)