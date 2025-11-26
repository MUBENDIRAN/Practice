s = input()
# for anagram char
p = input()
# to store the anagram char and their frequency
freq_p = {}
for ch in p :
    ''' this step adds the anagram char if not available by sending zero , if available add to freq dict with number one
    if again the same char found while iteration it addes +1 '''
    freq_p[ch] = freq_p.get(ch,0) + 1
# to store input string of char
freq_s = {}
start = 0
for end in range(len(s)):
    # similar to anagram we store string of char and its frequency in freq_s dict
    freq_s[s[end]] = freq_s.get(s[end],0) +1
    # if the anagram length found the first window is created and checked with comparison condition 
    if end - start + 1 == len(p):
        if freq_p == freq_s:
            print("Found")
        # after first window the first char of the window is made zero since not needed for the next iteration of window
        freq_s[s[start]] -= 1
        # if the first char of the window is zero delete is so no error is found during second iteration
        if freq_s[s[start]] == 0:
            del freq_s[s[start]]
        start += 1

