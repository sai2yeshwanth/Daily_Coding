# Split the sentence
# Given a list of N words, Write a program to print each Word in a line.
#The first line of input will contain space-separated word, denoting the elements of the list.


def split_sentence(sentence):
    
    list_a = sentence.split()  # convert sentence to a list using split() function
    #print(list_a)
    for word in list_a:
        print(word)
    
    
    return

sentence = input("Enter the sentence : ")
split_sentence(sentence)