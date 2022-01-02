# sum of even number from M to N

M = int(input("Enter the starting number : "))
N = int(input("Enter the ending number : "))

even = 0

for i in range(M,N+1):
    if (i%2)==0:
        even += i

print(even)