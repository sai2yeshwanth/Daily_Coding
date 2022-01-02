# Given an integer number(N) as input. Write a program to print the sum of first N natural number
#using while loop
N = int(input("Enter the N number : "))

add = 0
counter = 1
while counter <= N:
    add +=counter
    #print(add)
    counter+=1
print(add)