# perimeter of square
def perimeter_of_square(arg_1):
    # perimeter formula is p = 4a
    perimeter = arg_1*4
    perimeter = f"perimeter of given {arg_1} is {perimeter}" # using f-string 
    return perimeter
    
    
side = int(input("enter the side :"))
result = perimeter_of_square(side)
print(result)
