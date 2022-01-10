# Half pyramid pattern

def half_pyramid(number):

    for row in range(1,number+1):
        pattern = ""
        for col in range(1,row+1):
            pattern +=str(col)+" "
        print(pattern)

    return

number = int(input("Enter the number to print half pyramid : "))
half_pyramid(number) 