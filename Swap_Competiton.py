# Swap Competiton


def swap_competition(list_a):
    result = []
    for item in range(len(list_a)):
        words = list_a[item]
        first_word = item[0]
        second_word = item[1]
        first_word = list(first_word)
        second_word =list(second_word)
        first_word = sorted(first_word)
        second_word = sorted(second_word)
        if first_word == second_word:
            result.append("YES")
        else:
            result.append("NO")
    return result
        
        


list_a = []
T = int(input("Enter the number inputs :"))
for i in range(T):
    word_list = input("Enter the Words :").split()
    list_a.append(word_list)
    
result = swap_competition(list_a)
print(result)