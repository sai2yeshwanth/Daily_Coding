# Given an integer number(N) as input.write a program to print the sum of first natural number.
# using for-loop

N = int(input("Please enter the number to sum of first N natural number : "))

add = 0
for i in range(1,N+1):
    add +=i
print(add)
    