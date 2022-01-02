# given two integers M and N, Write a program to print the sum of the number from M to N

M = int(input("Enter the Mth number : "))
N = int(input("Enter the Nth Number : "))

add = 0
for i in range(M,N+1):
    add+=i
print(add)