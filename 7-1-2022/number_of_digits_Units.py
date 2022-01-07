# number of digit until N
# Given an Integer N, Write a program that prints the count of the Total number of digits between 1 and N.

def digits(N):
    string = ""
    for num in range(1,N+1):
        string += str(num)
    total = len(string)
    print(total)
    return
N = int(input("Enter the Number to find total number of digits : "))
digits(N)