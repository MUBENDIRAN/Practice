def merge_intervals(inter):
    if len(inter) == 0:
        return []

    inter.sort(key = lambda x: x[0])
    merge = [inter[0]]

    i = 1
    while i < len(inter):
        first = inter[i][0]
        last = inter[i][1]
        last_merge = merge[-1][1]

        if first <= last_merge:
            merge[-1][1] = max(last_merge,last)
        else:
            merge.append([first,last])

        i += 1

    return merge

row = int(input("how many intervals : "))
inter = []
for _ in range(row):
    i = list(map(int,input("Enter the sequence : ").split()))
    inter.append(i)
print("Merged :",merge_intervals(inter))
        
