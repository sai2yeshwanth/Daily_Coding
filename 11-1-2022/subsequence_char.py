# subsequence 

def Subsequence(full_string,sub_sequence):
    sub_index = 0
    sub_len = len(sub_sequence)
    for char in full_string:
        if char == sub_sequence[sub_index]:
            sub_index +=1
            if sub_index == sub_len:
                break
    if sub_index == sub_len:
        print("{0} is subsequence of {1}".format(full_string,sub_sequence))
    else:
        print("{0} is not subsequence of {1}".format(full_string,sub_sequence))
    
    
    return

full_string = input("Enter the word : ")
sub_sequence = input("Enter the subsequence word :  ")

Subsequence(full_string,sub_sequence)