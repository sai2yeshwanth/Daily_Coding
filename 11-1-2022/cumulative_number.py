# cumulative Sum 

def Cumulative_sum (number):
    cumulative_sum = 0
    for i in range(number):
        enter_number = int(input("Enter the number : "))
        cumulative_sum +=enter_number
        print("Sum of Cumulative number :",cumulative_sum)
        
    
    return

number = int(input("Enter the number of  line : "))
Cumulative_sum(number)