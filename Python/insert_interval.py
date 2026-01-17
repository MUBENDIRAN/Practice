# this function holds the operation of inserting the new interval into existing which is sorted 
def insert_interval(inter,new_inter):
    res = [] # stores the final interval after insertion
    i = 0 
    n = len(inter)
    # if there is no overlapping its already an complete interval so just the interval is appends
    while i < n  and inter[i][1] <= new_inter[0]:
        res.append(inter[i])
        i += 1
    # if there is an overlapping its gets resolved and new interval is generated and appended to res 
    while i < n and inter[i][0] <= new_inter[1]:
        new_inter[0] = min(new_inter[0],inter[i][0])
        new_inter[1] = max(new_inter[1],inter[i][1])
        i += 1
    res.append(new_inter)
    # after the insertion other intervals are added to res to make the final inserted and sorted intervals
    while i < n:
        res.append(inter[i])
        i += 1

    return res 
# custom input 
row = int(input("Enter the number of intervals : "))
inter = []
for _ in range(row):
    i = list(map(int,input("Enter the sequence : ").split()))
    inter.append(i)
# custom input
new_inter = list(map(int,input("Enter the new sequence : ").split()))
print("Inserted",insert_interval(inter,new_inter))