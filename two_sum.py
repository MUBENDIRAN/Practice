def two_sum(nums,target):
    seen = {}

    for i in range(len(nums)):
        num  = nums[i]
        need = target - num
        if need in seen:
            return (seen[need],i)
        seen[num] = i

nums  = list(map(int,input("Enter the sequence : ").split()))
target = int(input("Enter the target number : "))
print("The sum indices are :",two_sum(nums,target))
