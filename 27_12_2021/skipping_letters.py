# You's given a word and an index posistion of a character.
# You need to write a program that prints the given word without the character at given index.

word = input("Enter the Word : ")

print("Enter the index to Skip the character")
index = int(input())

before = word[:index]
after = word[index+1:]

result = before + after

print(result)
