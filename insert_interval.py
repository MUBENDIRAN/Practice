def insert_interval(inter,new_inter):
    res = []
    i = 0
    n = len(inter)

    while i < n  and inter[i][1] <= new_inter[0]:
        res.append(inter[i])
        i += 1

    while i < n and inter[i][0] <= new_inter[1]:
        new_inter[0] = min(new_inter[0],inter[i][0])
        new_inter[1] = max(new_inter[1],inter[i][1])
        i += 1
    res.append(new_inter)

    while i < n:
        res.append(inter[i])
        i += 1

    return res 

row = int(input("Enter the number of intervals : "))
inter = []
for _ in range(row):
    i = list(map(int,input("Enter the sequence : ").split()))
    inter.append(i)

new_inter = list(map(int,input("Enter the new sequence : ").split()))
print("Inserted",insert_interval(inter,new_inter))