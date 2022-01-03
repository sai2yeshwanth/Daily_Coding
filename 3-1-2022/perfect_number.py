# perfect number
# a number is considered as a perfect number if sum of all factors excluding itself is equal to the number.

factors_number = int(input("Enter the number : "))

sum_of_factors = 0

for num in range(1,factors_number):
    if (factors_number%num )==0:
        sum_of_factors += num
        
if sum_of_factors == factors_number:
    print("Perfect Number")
else:
    print("Not a Perfect Number")