# solid Right Angled Tringle-2

def Solid_Right_Angled_tringle(number):
    K = number
    for row in range(1,number+1):
        pattern = ""
        for col in range(1,row+1):
            space = "  "*(K-row)
            star = "* "*col
        print(space+star)
        
    return

number = int(input("Enter the number to print number : "))
Solid_Right_Angled_tringle(number)