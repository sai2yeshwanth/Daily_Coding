# Write a program to print the smallest value among the three numbers A,B, and C

A = int(input())
B = int(input())
C = int(input())

condition_one = (A <= B) and (A <= C)
condition_two = (B <= A) and (B <= C)

if condition_one:
    print(A)
elif condition_two:
    print(B)
else:
    print(C)