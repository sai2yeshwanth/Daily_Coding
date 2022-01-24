# Nested list Indexing

num_list = [(2, 4, 6, 8), (5, 15, 25, 35), (7, 14, 21)]
print(f"num_list = {num_list}")

# Write your code here

n = int(input("Enter the Number in num_list :"))

for tuple_a in num_list:
    if n in tuple_a:
        tuple_index = num_list.index(tuple_a)
        n_index = tuple_a.index(n)
        print(f"{n} in {tuple_index} {n_index}")