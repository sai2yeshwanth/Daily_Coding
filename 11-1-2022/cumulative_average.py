# Cumulative Average 

def Cumulative_Average(number):
    
    cumulative_average = 0
    for i in range(1,number+1):
        input_number = int(input("Enter the number : "))
        cumulative_average+=input_number
        average = round(cumulative_average/i, 3)
        print("Average of the cumulative :",average)
    
    
    return

number = int(input("Enter the no of number: "))
Cumulative_Average(number)