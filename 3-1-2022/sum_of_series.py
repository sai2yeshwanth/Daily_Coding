#sum of the series
# Write a program to find the sum of the series 2+22+222+2222 N terms

N =  int(input("Enter the length of the series : "))

term_number = "2"
total = 0

for i in range(1,N+1):
    term = term_number*i
    total += int(term)
print("Sum of the series of 2 is : ",total)