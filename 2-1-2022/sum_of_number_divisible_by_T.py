# sum of Numbers divisible by T

T = int(input("Enter the divided number : "))
M = int(input("Enter the starting number : "))
N = int(input("Enter the ending number : "))

divisible = 0

for i in range(M,N+1):
    if (i%T)==0:
        divisible += i
        
print(divisible)