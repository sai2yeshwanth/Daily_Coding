# prime number 
# print prime number in N natural Number

def prime_number(number):


    for i in range(2,number+1):
        counter = 0
        for j in range(2,i-1):
            if (i%j) ==0:
                counter +=1
        if counter == 0:
            print(i)

    return

number=int(input("Enten the range of the N natural number : "))
prime_number(number)