# Write a program to increment N by5, if N is  greater than 10, otherwise by 1

number = int(input())

condation = number >10

if condation:
    number+=5
else:
    number+=1

print(number)