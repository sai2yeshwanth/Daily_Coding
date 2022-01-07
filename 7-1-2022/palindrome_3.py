# penlindrome or not
# ignore the spaces, quotes, case sensitive

def penlindrome(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace(" ","")
    
    modified_sentence = ""
    for char in sentence:
        modified_sentence = char + modified_sentence
    
    if modified_sentence == sentence:
        print(True,"It's a palindrome")
    else:
        print(False,"It's not a penlindrome")

    return

sentence = input("Enter the sentence : ")
penlindrome(sentence)