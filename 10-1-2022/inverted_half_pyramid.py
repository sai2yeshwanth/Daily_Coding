#inverted half pyramid

def inverted_half_pyramid(number):

    for row in range(number):
        pattern = ""
        k = number-row
        for col in range(1,k+1):
            pattern = pattern +(str(col)+" ")
        print(pattern)

    return

number = int(input("Enter the number to print Inverted Half Pyramid : "))
inverted_half_pyramid(number)