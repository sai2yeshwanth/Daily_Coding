N = int(input("Please Enter the number :  "))

factorial = 1

for i in range(1,N+1):
    factorial *=i
print("The factorial of given number",factorial)