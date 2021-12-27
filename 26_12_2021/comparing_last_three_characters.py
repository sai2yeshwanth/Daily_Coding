
# write a program to cheak if the last three characters in the two given strings are the same

first_word = input("Enter the first word : ")
second_word = input("Enter the second word : ")

first_word = first_word.lower() #convert to lowercase
second_word =second_word.lower() #covert to lowercase

length_first_word = len(first_word) #finding length of the string
length_second_word = len(second_word) # finding length of the string

indexing_first_word = first_word[length_first_word-3:]
indexing_second_word = second_word[length_second_word-3:]

if indexing_first_word==indexing_second_word: #comparing the last three character of given two words
    print(True)
else:
    print(False)