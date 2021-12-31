year  = int(input("Enter the year : "))

if year % 4 == 0 and  year % 100 != 0:
    print(year,"is a leap year",True)
else :
    print(year,"is not leap year",False)