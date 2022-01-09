# Numbers in Rectangular pattern - 1
# write a program to print numbers from 1 to N in each row forming a rectangular pattern of M rows ans N columns

def numbers_in_rectangular_pattern(rows,columns):
    print("{0} rows and {1} numbers in a row".format(rows, columns))
    nums = ""
    for i in range(1,columns+1):
        nums += str(i)+" "
    for i in range(rows):
        print(nums)
    
    return

rows = int(input("Enter the number rows to print : "))
columns = int(input("Enter the numbers in a row : "))

numbers_in_rectangular_pattern(rows,columns)