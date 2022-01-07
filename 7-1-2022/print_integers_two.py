# print integers
# given an integer N. Write a program to print integer N to 1
# for example N = 5
# then the output will be 
# 5
# 4
# 3
# 2
# 1 

def print_integer(N):
    for num in range(N):
        print(N-num)

N =int(input("Enter the number to Print N to 1 : "))
print_integer(N)
                     