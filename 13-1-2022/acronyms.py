# Acronyms

def acronyms(sentence):
    
    new_list =[]
    for i in range(len(sentence)):
        new_list.append(sentence[i][0])
    
    new_list = ".".join(new_list)
    
    return new_list

sentence = input("Enter the Acronyms : ").split()
result = acronyms(sentence)
print("Acronyms {}".format(result))