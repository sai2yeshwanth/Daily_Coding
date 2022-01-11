# Double Char

def double_char (word):
    
    double_character = ""
    for i in word:
        double_character += str(i*2)
    print("Double characters of {} is {}".format(word,double_character))
    return

word = input("Enter the Word : ")
double_char(word)