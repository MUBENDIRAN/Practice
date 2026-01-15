def top_k_element(nums,k):
    freq = {}
    for x in nums:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    bucket = []
    for _ in range(len(nums) + 1):
        bucket.append([])

    for n in freq.items():
        num = n[0]
        f = n[1]
        bucket[f].append(num)

    res = []
    for f in range(len(nums) - 1,0,-1):
        for num in bucket[f]:
            res.append(num)
            if len(res) == k:
                return res

nums = list(map(int,input("Enter the sequenece : ").split()))
k = int(input("Enter the value : "))
print("The top elements are :",top_k_element(nums,k))