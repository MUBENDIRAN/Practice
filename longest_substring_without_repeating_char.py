s = input()
last_seen = {}
start = 0
max_len = 0
for end in range(len(s)):
    if s[end] in last_seen and last_seen[s[end]] >= start:
       start = last_seen[s[end]] + 1
    last_seen[s[end]] = end
    max_len = max(max_len , end - start + 1)
print(max_len)
