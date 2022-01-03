# Armstrong number 

number = input("Enter the number to find of if it's Armstrong Number or Not :\n")

length_of_number = len(number)
power_of_number = 0

for num in number:
    converting = int(num)
    power_of_number += converting**length_of_number
    
if int(number)==power_of_number:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")