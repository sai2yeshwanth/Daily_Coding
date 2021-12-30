# Permission To Attend Exam or not

percentage_of_attendance = input("Enter the Percentage of attendance \n")        # input well be 70% like these
medical_Report = input("If you have any medical report type Y or type N \n").upper()                  # input well Yes(Y) or No(N)

len_percentage_of_attendance = len(percentage_of_attendance)
attendance = int(percentage_of_attendance[:len_percentage_of_attendance-1])

condition_one = (attendance >= 75) 
condation_two = (attendance < 75) and (medical_Report == "Y")

if condation_two :
    print("Allowed to write exam")
elif condition_one:
    print("Allowed to write exam")
else:
    print("Cannot write exam")
