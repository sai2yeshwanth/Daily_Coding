# Maximum 
# You ar given N number of inputs. Print the maximun of them after each input.

def maximum(number):
    print("Displaying maximun in the input")
    maximum_number = 0
    for num in range(number):
        input_number = int(input("input : "))
        if maximum_number <= input_number:
            maximum_number = input_number
        print("maximum input :",maximum_number)
    
    return 

number = int(input("Enter the no of numbers : "))

maximum(number)