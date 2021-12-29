# Write a program to print the sum of two numbers, A and B. If their sum is less than 10,
# otherwise print the product of numbers

A = int(input())
B = int(input())

condition = (A+B <= 10)

if condition:
    ans = A+B
else:
    ans = A*B

print(ans)