# Four Passengers and a Driver
# A typical car can hold four passengers and one driver, allowing five people to travel around.
# Write a function with the name number_of_cars_needed that takes a number of people(N) and return how many cars are needed to seat everyone comfortably.


def number_of_cars_needed(no_of_people):
    # writing  the function
    no_of_cars = no_of_people//5
    remining_cars = no_of_people%5
    if remining_cars > 0:
        no_of_cars += 1
    return f"'{no_of_cars}' cars"

no_of_people = int(input("Enter the peeple : "))
# Call the number_of_cars_needed function
result = number_of_cars_needed(no_of_people)
print(result)