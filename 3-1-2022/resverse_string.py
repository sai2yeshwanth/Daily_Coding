# Reverse string
# Write a program to print a reverse in string.

string = input("Enter the word or sentence to print in reverse order \n ")

reverse_string = ""

for char in string:
    reverse_string = char +reverse_string

print("Reverse word or sectence  ")
print(reverse_string)