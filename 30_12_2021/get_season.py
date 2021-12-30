# Write a program to find season for the given month number.

month = int(input("Enter the Month Number \n"))

Winter = (month == 12) or (month == 11) or (month ==1)
Spring = (month == 2) or (month == 3)
Summer = (month == 4) or (month == 5) or (month == 6)
Rainy = (month == 7) or (month ==8)
Autumn = (month == 9) or (month == 10)

if Winter:
    print("Winter")
elif Spring:
    print("Spring")
elif Summer:
    print("Summer")
elif Rainy:
    print("Rainy")
elif Autumn:
    print("Autumn")
else:
    print("Invalid Month")