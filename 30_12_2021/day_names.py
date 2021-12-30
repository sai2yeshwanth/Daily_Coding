# given day number D as input, Write a program to display the day name.
# (1-Monday, 2-Tuesday, 3-wednesday, 4-Thursday, 5-Friday, 6-Saturday, 7-Sunday )


Day = int(input("Enter the Day : \n"))

if Day==1:
    print("Monday")
elif Day == 2:
    print("Tuesday")
elif Day == 3:
    print("Wednesday")
elif Day ==4:
    print("Thursday")
elif Day ==5:
    print("Friday")
elif Day==6:
    print("Saturday")
elif Day ==7:
    print("Sunday")
else:
    print("Invaild Day")