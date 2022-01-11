# Convert string to list

def convert_string_to_list(word):
    list_a = list(word)
    print("The word {} is covernt to list {}".format(word,list_a))
    
    return
word = input("Enter the word to convert into list : ")
convert_string_to_list(word)