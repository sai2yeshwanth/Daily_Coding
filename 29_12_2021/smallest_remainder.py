# you are given two integers, a and b . print the smallest Value among a%b and b%a

print("Enter the Number : ")
A = int(input())
B = int(input())

condation = (A%B) > (B%A)
 
print("Smallest remainder is")
if condation:
    print(B%A)
else:
    print(A%B)