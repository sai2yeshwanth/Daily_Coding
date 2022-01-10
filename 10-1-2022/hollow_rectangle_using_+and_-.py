# Hollow Rectangle -2
# write a program to print a rectangle pattern of M rows and N columns using the character as shown below.

def hollow_rectangle(M,N):
    print("{} X {} Hollow Rectangle Pattern using + and - ".format(M,N))
    top_and_bottom = "+"+("-"*N)+"+"
    print(top_and_bottom)
    for i in range(M):
        space = " "*N
        print("|"+space+"|")
    print(top_and_bottom)
    
    
    return
M = int(input("Enter the Number of Rows : "))
N = int(input("Enter the Number of Columns : "))

hollow_rectangle(M,N)