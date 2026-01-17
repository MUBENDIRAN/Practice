# this function handles operation of best pairs of target to sum
def two_sum(nums,target):
    seen = {} # holds the unqiue subtracted value for future reference

    for i in range(len(nums)): 
        num  = nums[i]
        need = target - num # this creates the unique subtracted value
        if need in seen: # if the unique subtracted value is already found then current and found is the best two sum pair
            return (seen[need],i)
        seen[num] = i # if not found its added to seen for future reference
# custom input
nums  = list(map(int,input("Enter the sequence : ").split()))
target = int(input("Enter the target number : "))
print("The sum indices are :",two_sum(nums,target))
