# labelling Numbers

def show_numbers(number):
    
    for num in range(number+1):
        if (num%2) == 0:
            print(f"{num} EVEN")
        else:
            print(f"{num} ODD")
    
    

number = int(input("Enter the number range : "))
# Call the show_numbers function
show_numbers(number)