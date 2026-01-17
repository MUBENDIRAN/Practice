arr = list(map(int,input().split()))
# to store the prefix sumed value one by one during loop
prefix = []
# store the live iterated value
max_sum = 0
for x in arr:
    # it sums with the previous(prefix) value 
    max_sum += x
    # it appended and modifies untill loop runs
    prefix.append(max_sum)
print(max_sum)