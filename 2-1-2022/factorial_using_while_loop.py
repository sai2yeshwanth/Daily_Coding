N = int(input("Please enter the number : "))

factorial = 1
counter = 1
while counter <= N:
    factorial*=counter
    counter+=1
print("The Factorial of the given number : ",factorial)