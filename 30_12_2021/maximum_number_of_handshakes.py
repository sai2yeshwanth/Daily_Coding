n = int(input("Enter the number of Students\n"))

hand_shakes = 0 
for i in range(n):
    hand_shakes += i
    
print("Number of handshakes are {}".format(hand_shakes))