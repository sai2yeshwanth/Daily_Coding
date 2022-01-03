# factors of a number 

#write a program to print the factors of the given number

number = int(input("Enter the Number : "))

print("The numbers divisible by {} is ".format(number))
for num in range(1,number+1):
    if (number % num) == 0:
        print(num)