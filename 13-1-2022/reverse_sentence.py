# Reverse the sentence

def reverse_sentence(sentence):
    
    sentence = sentence[::-1]
    modified_sentence = " ".join(sentence)
    
    return modified_sentence

sentence = input("Enter the sentence : \n").split()
result = reverse_sentence(sentence)
print("modified sentence :\n"+result)