# perfect squares in a range
# you are given two given number, A and B where 1 <= A <= B, Write a program to find the 
# number of perfect squares in the range A to B (including A and B).

def perfect_squares(A,B):
    counter = 0
    
    for num in range(A,B+1):
        check_num = 1
        while check_num*check_num <=num:
            if check_num*check_num == num:
                counter+=1
            check_num+=1
        
    print("There are {0} Perfect squares in a range of {1} to {2}".format(counter,A,B))
    return


A = int(input("Enter the first Number : "))
B = int(input("Enter the secound Number : "))
perfect_squares(A,B)