# write a program to print if the given number is divible by any of the luckey number6,3,2
# in decreasing order of priority(6 is luckier than 3 aand 3 is luckier than 2) not number is not divible by 2,3,6

print("Enter the Number : ")
number = int(input())

if (number % 6) == 0:
    print("Number is divisible by 6")
elif (number % 3) == 0:
    print("Number is divisible by 3")
elif (number % 2) == 0:
    print("Number is divisible by 2")
else:
    print("Number is not divisible by 2, 3 or 6")