# given an integer N, write a program which read N inputs and prints them
# using while_loop


N = int(input("Enter the number of inputs to read : "))

counter = 1
while counter <= N:
    inputs = input("Enter the input to read : ")
    counter +=1
    print(inputs)