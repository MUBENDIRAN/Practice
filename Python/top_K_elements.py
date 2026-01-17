# this function holds the operation of finding the top frequently repeated elements in the list 
def top_k_element(nums,k):
    freq = {} # this stores the element and its frequency 
    for x in nums:
        if x in freq:
            freq[x] += 1 # this adds the frequency + 1 if already available 
        else:
            freq[x] = 1 # if not already add with frequecy with one 
    
    bucket = [] # this stores the frequecy and and its number mapped in the descending order 
    for _ in range(len(nums) + 1): # we have created len + 1 since maintain edge cases 
        bucket.append([])

    for n in freq.items(): # iterate through the frequency 
        num = n[0] # num stores the value 
        f = n[1] # f stores the frequency
        bucket[f].append(num) # frequency is mapped to num value 

    res = [] # this stores the top k elements
    for f in range(len(nums) - 1,0,-1): # we are iterating through backwards since frequency values are descending 
        for num in bucket[f]: # with the first found frequecy its value is added to res 
            res.append(num)
            if len(res) == k:   # when length of res matches the value of k the result is obtained 
                return res
# custom input 
nums = list(map(int,input("Enter the sequenece : ").split()))
k = int(input("Enter the value : "))
print("The top elements are :",top_k_element(nums,k))