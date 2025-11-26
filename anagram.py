s = input()
p = input()
freq_p = {}
for ch in p :
    freq_p[ch] = freq_p(ch,0) + 1
    print(freq_p)
