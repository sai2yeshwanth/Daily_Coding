# composite number

def composite_number(number):
    if number > 1:
        counter = 0
    else:
        counter = 1
        
    for num in range(2,number):
        if (number%num) == 0:
            counter += 1
    if not(counter == 0):
        print("{} is composite number".format(number))
    else:
        print("{} is not composie number".format(number))
    
    return
number = int(input("Enter the number : "))
composite_number(number)