# Sum of odd Number from M to Number

M = int(input("Enter the starting number : "))
N = int(input("Enter the ending number : "))

odd = 0

for i in range(M,N+1):
    if (i%2)!=0:
        odd +=i
print(odd)