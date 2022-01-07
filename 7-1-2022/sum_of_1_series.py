# Sum of 1 series 
# Given integer N as input. Write a program to print the sum of series 1 + 11 + 111 +... N terms.

def sum_of_series(N):
    sum_of_1_series = 0

    for num in range(1,N+1):
        string = "1"*num
        covernting_string_to_integer = int(string) 
        #print(type(covernting_string_to_integer))
        #print(covernting_string_to_integer)
        sum_of_1_series+=covernting_string_to_integer

    print(sum_of_1_series)
    
N = int(input("Enter the Number "))
sum_of_series(N)