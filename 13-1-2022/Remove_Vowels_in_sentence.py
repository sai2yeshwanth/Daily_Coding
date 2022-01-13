# Remove Vowels in a sentence

def remove_vowels_in_a_sentence(sentence):
    
    
    vowels = "aeiouAEIOU"
    
    for char in vowels:
        sentence = sentence.replace(char,"")
    print("Remove all vowels in sentence :\n{}".format(sentence))
    
    
    return

sentence = input("Enter the sentens : \n")
remove_vowels_in_a_sentence(sentence)