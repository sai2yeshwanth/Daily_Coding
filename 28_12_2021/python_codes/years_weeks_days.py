#Given N number of days as input,
# write a program to convert N number of days to years(Y) weeks(W) and days(D)


print("Enter the days:")
num = int(input())

years = num//365 # conver the days to years
weeks = (num%365)//7
days = (num % 365) % 7 

print(years,"Years ",weeks,"Weeks ",days,"Days")