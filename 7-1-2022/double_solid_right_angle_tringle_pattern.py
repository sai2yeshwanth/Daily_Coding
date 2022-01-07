# Solid Right angled Tringle-2
# Given the Integer number N as input. Write a program to print the double Tringlar pattern of N lines using astrisk(*)
# Character as shown below. 
# Note: There is space after each astrisk * character 
# eg : N=2
# *
# * *
# *
# * *


def solidRight(N):
    for i in range(1,N+1):
        print("* "*i)
    return

N = int(input("Enter the Number to print the solid Right angled tringle : "))
solidRight(N)
solidRight(N)