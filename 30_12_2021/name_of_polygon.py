# Give the number if size. write a program to print the name of the polygon

polygon = int(input("Enter the size : "))

N = (polygon < 3)
T = (polygon == 3)
Q = (4 == polygon)
P = (5 == polygon)
B = (polygon > 5)

if N:
    print("Not Polygon")
elif T:
    print("Triangle")
elif Q:
    print("Quadrilateral")
elif P:
    print("Pentagon")
elif B:
    print("Big Polygon")
    
