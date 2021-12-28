#Write a program that reads a single line of input and prints the first two and last
#two character of the given input and prints the asterisk character(*) in place of the
#remaining characters

print("Enter the Word:")
word = input()

length_of_the_word = len(word)

before = word[:2]
after = word[-2:]
asterisk = length_of_the_word-4

print(before+(asterisk*"*")+after)

#input = message
#output = me***age