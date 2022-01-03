# Hollow Square Pattern using the Asterisk character(*)

N = int(input("Enter the number \n"))

for i in range(N):
    if (i==0) or (i==(N-1)):
        print("* "*N)
    else:
        N_of_space = ("  "*(N-2))
        print("* "+N_of_space+"* ")