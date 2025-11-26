s = input()
p = input()
freq_p = {}
for ch in p :
    freq_p[ch] = freq_p.get(ch,0) + 1
freq_s = {}
start = 0
for end in range(len(s)):
    freq_s[s[end]] = freq_s.get(s[end],0) +1
    if end - start + 1 == len(p):
        if freq_p == freq_s:
            print("Found")
            freq_s[s[start]] -= 1
            if freq_s[s[start]] == 0:
                del freq_s[s[start]]
            start += 1

