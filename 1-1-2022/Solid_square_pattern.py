#Print the solid Square pattern of N number of rows and columns
# using While-loop

N = int(input("Enter the number : "))

counter = 1
while counter <= N:
    print("* " * N)
    counter += 1