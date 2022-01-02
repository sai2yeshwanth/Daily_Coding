# Write a program that read a word and print each character of the word in a new line
# usind
string = input("Enter the word : ")

len_of_string = len(string)

counter = 0
while counter <= len_of_string-1:
    print(string[counter])
    counter+=1