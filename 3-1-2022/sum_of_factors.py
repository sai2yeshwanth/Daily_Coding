#sum of all factors
#write a program to print the sum of the all factors for a given number

factors_number = int(input("Enter the number : "))

sum_of_factors = 0

print("Sum of factors of {} number is".format(factors_number))
for num in range(1,factors_number+1):
    if (factors_number%num) == 0:
        sum_of_factors = sum_of_factors+num
        
print(sum_of_factors)