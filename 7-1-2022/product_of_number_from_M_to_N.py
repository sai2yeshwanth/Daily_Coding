# product of numbers from M to N

def product_of_number(M,N):
    product = 1
    for num in range(M,N+1):
        product *= num
    print(product)
    return

M = int(input("Enter the Starting Number : "))
N = int(input("Enter the Ending number : "))

product_of_number(M,N)