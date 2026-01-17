s = input()
# this dict is to store the unique values of s 
last_seen = {}
start = 0
# to count the len of longest substring
max_len = 0
for end in range(len(s)):
    # condition : if the iterated element is found in last_seen dict and its value is more than once 
    if s[end] in last_seen and last_seen[s[end]] >= start:
        # move towards right so start is increased by the element found from
       start = last_seen[s[end]] + 1
    # this to modify the number of times the element found in s stored in dict
    last_seen[s[end]] = end
    # using max fuction the previous and current iterated value is compared and the maximum value is stored 
    max_len = max(max_len , end - start + 1)
print(max_len)
