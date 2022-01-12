# Reverse the letters in words of the sectence

def reverse_letters(sentence):
    
    reverse_list = []
    for word in sentence:
        reverse_list.append(word[::-1])
    
    modified_sectence = " ".join(reverse_list)
    print("Reverse the letters in words of sentence : \n{}".format(modified_sectence))
    
    return

sentence = input("Enter the sentence : \n").split()
reverse_letters(sentence)