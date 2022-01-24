#Accessing Nested Lists

list_a = [('apple', 'banana', 'orange', 'grapes'), ('cricket', 'football', 'hockey'), ('car', 'bicycle', 'bus')]
# Write your code here
print(f"list_a = {list_a}")
n = int(input("Enter the Number of input : "))
new_list =[]
for i in range(n):
    m,n = input("Enter the index Values : ").split()
    m ,n = int(m),int(n)
    value_index = list_a[m][n]
    new_list.append(value_index)
print(new_list)
    