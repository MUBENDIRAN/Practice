# this function holds the opertion of merging the intervals which is unsorted 
def merge_intervals(inter):
    # to handle the edge cases
    if len(inter) == 0:
        return []
    # since its unsorted we sort using the first value 
    inter.sort(key = lambda x: x[0])
    # the first interval is added to merge after sorting 
    merge = [inter[0]]
    # since the first is already merged we start from second so 1 
    i = 1
    while i < len(inter):
        first = inter[i][0] # first is first value of  interval of second interval
        last = inter[i][1] # last is next value of  interval of second interval
        last_merge = merge[-1][1] # last_merge is the last value of overall interval
    # if there is chance of merging its merged 
        if first <= last_merge:
            merge[-1][1] = max(last_merge,last)
        else:
            merge.append([first,last]) # if there is no chance of merging append to merge as its already merged

        i += 1

    return merge
# custom input
row = int(input("how many intervals : "))
inter = []
for _ in range(row):
    i = list(map(int,input("Enter the sequence : ").split()))
    inter.append(i)
print("Merged :",merge_intervals(inter))
        
