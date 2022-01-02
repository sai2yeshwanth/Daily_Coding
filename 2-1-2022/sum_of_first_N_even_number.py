# Sum of First N even number 

N = int(input("Enter the Nth Number to add even number : "))

even = 0

for i in range(N+1):
    if (i%2)==0:
        even +=i
print(even)