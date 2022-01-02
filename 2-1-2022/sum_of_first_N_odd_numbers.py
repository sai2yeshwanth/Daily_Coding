# sum of first N odd numbers

N = int(input("Enter the number : "))

odd = 0

for i in range (N):
    if i%2 != 0:
        odd+=i
print(odd)
