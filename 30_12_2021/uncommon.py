# Given a number N, find whether the number is common or uncommon. A number is considered uncommon if 
# it is not divisible by any single-digit prime


number = int(input("Enter the number : "))

condition = (number%2==0 or number%3==0 or number%5==0 or number%7==0 )

if condition:
    print(False)
else:
   print(True)