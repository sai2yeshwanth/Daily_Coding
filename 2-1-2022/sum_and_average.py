# sum and average of the 10 numbers

add = 0

for i in range(10):
    input_numbers = int(input("Enter the number : "))
    add += input_numbers
    average = add/10
print("Sum of ten numbers :",add)
print("Average of ten numbers :",average)
    
    