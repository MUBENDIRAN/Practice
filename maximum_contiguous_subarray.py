def subarray(nums):
    curr_max = nums[0]
    max_sum = nums[0]

    for i in range(1,len(nums)):
        curr_max = max(nums[i],curr_max + nums[i])
        max_sum = max(max_sum,curr_max)

    return max_sum

nums = list(map(int,input("Enter the sequence : ").split()))
print("Max value of contiguous subarray :",subarray(nums))