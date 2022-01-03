# smallest among n number

N = int(input("Enter the numbers :"))

first_number = int(input())
smallest_number = first_number

for i in range(N-1):
    num = int(input())
    if smallest_number>num:
        smallest_number = num
        
print(smallest_number)