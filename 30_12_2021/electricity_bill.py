# Electricity Bill

units = int(input("Enter the units\n"))

bill =0

if units < 50:
    bill = units * 2
elif units < 150:
    bill = (50 * 2) +(3*(units-50))
elif units < 250:
    bill = (50 * 2) +(3*100)+(5*(units-150))
elif units >= 250:
    bill = (50 * 2) +(3*100)+(5*100)+(8*(units-250))
    
subcharge =(0.2*bill)
total_bill = (bill + subcharge)
print(total_bill)
