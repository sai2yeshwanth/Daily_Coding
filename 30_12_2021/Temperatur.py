# Write a program to display a customized message based on temperature T

T = float(input("Enter the temperature \n"))

if T < 0:
    print("Freezing weather")
elif (0 <= T) and (T < 10):
    print("Very Cold weather")
elif (10 <= T) and (T<20):
    print("Cold weather")
elif (20 <= T) and(T<30):
    print("Normal")
elif(30<=T) and(T <40):
    print("Hot")
elif(T>=40):
    print("Very Hot")