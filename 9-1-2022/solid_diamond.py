# solid diamond 
# write a program to print a solid diamond pattern of 2N-1 rows using the asterisk character(*)

def solid_diamond(number):
    k = number-1
    for i in range(1,number+1):
        spaces = " "*k
        stars = "* "*i
        print(spaces+stars)
        k-=i
    k=number
    for i in range(1,number):
        spaces = " "*i
        stars = "* "*(k-i)
        print(spaces+stars)
        


        

    return

number = int(input("Enter the number to form the diamond shape to make : "))
solid_diamond(number)