# sum of squares

N = int(input("Enter the number : "))

sum_of_squares = 0

for i  in range(N+1):
    sum_of_squares += (i**2)
    
print(sum_of_squares)
    