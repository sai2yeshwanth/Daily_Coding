# list Reverse
# Given a list of word, write program to reverse the words in the list.

def list_reverse(sentence):
    
    sentence = sentence[::-1] # using Reverse indexing
    print(sentence)
    
    return

sentence = input("Enter the sentence : ").split() # convert string to list using split() function

list_reverse(sentence)
