# this function holds the operation of kadanae algorithm of contiguous subarray
def subarray(nums):
    curr_max = nums[0] # initial dummy value
    max_sum = nums[0] # initial dummy value 
    # since the first value is already is assigned to curr_max and max_sum to handle edge cases of single value so index start from 1
    for i in range(1,len(nums)):
        curr_max = max(nums[i],curr_max + nums[i]) # if curr_max is negative then it affects next comming values so ignored and next value act as starting point
        max_sum = max(max_sum,curr_max) # this holds the latest max value 

    return max_sum
# custom input 
nums = list(map(int,input("Enter the sequence : ").split()))
print("Max value of contiguous subarray :",subarray(nums))