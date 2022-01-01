list_1 = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

days = input("Enter the days starting with : ")
date = int(input("Enter the date : "))

i = (date%7)-1   

if days in list_1:
    j = list_1.index(days)+i
    if j >=7:
        j = j-7
    print(list_1[j])