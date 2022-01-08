# World Tringle
# Given a Word, Write a program to print substrings in the expected pattern of N rows,
# Where N is the Length of word.

def word_tringle(N):
    string = ""
    for char in N:
        string += char
        print(string)
    return

word  = input("Enter the word to print in tringle format : ")
word_tringle(word)

