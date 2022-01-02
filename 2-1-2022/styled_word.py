# Write a program that prints the individual characters of the given word separated with hyphens("-").

word = input("Plese enter the word\t:")

lenght_of_word = len(word)

styled_word = word[0]

for i in range(1,lenght_of_word):
    styled_word = styled_word + "-" +word[i]

print(styled_word)