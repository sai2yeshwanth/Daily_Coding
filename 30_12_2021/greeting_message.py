# Write a program to prine a greeting message based on the given time.

time = int(input("Enter the time : "))

if (time >= 4) and (time <12):
    print("Good Morning")
elif (time >= 12) and (time <16):
    print("Good Afternoon")
elif (time >= 16) and(time < 20):
    print("Good Evening")
else:
    print("Good Night")