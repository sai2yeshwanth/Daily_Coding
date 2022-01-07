# Sum of K powers
# Write a program to print the sum of the Kth Power of the first N Natrul numbers.

def kth_power(N):
    sum_of_k_power = 0
    power = int(input("Power of the Number : "))               #power 
    for num in range(1,N+1):
        sum_of_k_power += (num**power)  
    print(sum_of_k_power)
    return 


N = int(input("Enter the Number : "))
kth_power(N)