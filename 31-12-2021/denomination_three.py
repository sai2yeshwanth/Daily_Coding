# Given an amount, Write a program to find the minimum number of note of different denominations that sum of the given amount.
# Available note denominations are 2000,500,200,50,20,5,2,1

amount = int(input("Please enter the amount\n"))

note_2000 = 0
note_500 = 0
note_200 = 0
note_50 = 0
note_20 = 0
note_5 = 0
note_2 = 0
note_1 = 0

if amount >= 2000:
    note_2000 = int(amount/2000)
    amount = int(amount%2000)
    
if amount >= 500:
    note_500 = int(amount/500)
    amount = int(amount%500)

if amount >= 200:
    note_200 = int(amount/200)
    amount = int(amount%200)

if amount >= 50:
    note_50 = int(amount/50)
    amount = int(amount%50)

if amount >= 20:
    note_20 = int(amount/20)
    amount = int(amount%20)
if amount >= 5:
    note_5 = int(amount/5)
    amount = int(amount%5)
    
if amount >=2 :
    note_2 = int(amount/2)
    amount = int(amount%2)

if amount >= 1:
    note_1 = amount

print("2000:"+str(note_2000)+" 500:"+str(note_500)+" 200:"+str(note_200)+" 50:"+str(note_50)+" 20:"+str(note_20)+" 5:"+str(note_5)+" 2:"+str(note_2)+" 1:"+str(note_1))