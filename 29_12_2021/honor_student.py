# In a School, the studends are divided into two categories based on their Ranks.
# Students whose rank is less than 10 are considered as HONER STUDENT and all others are
# considered as NORMAL STUDENT. Based on the Ranke, find to which category a student belongs.

rank = int(input())

condition = (rank in range(10))

if condition:
    print("HONOR STUDENT")
else:
    print("NORMAL STUDENT")