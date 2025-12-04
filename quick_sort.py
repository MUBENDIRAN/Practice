arr = list(map(int,input().split()))
# here low is 0 and high is last element 
def partition(arr,low,high):
    # since quick sort uses pivot to compare and  sort we use last element as pivot not a random
    pivot = arr[high]
    # it uses -1 to compare from begining as we go through last to first 
    i = low - 1
    for j in range(low,high):
        # if the iterated element is lesser its swaped and i is moved to next for comparison
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j], arr[i]
        # after all comparison the pivot element is set to its correct position according to the current sort
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i + 1
# this function execute the quick sort part
def quicksort(arr,low,high):
    # if the initial left side element is lesser than right 
    if low < high:
    # with pivot element we used in all function as centre the array is made to two parts for individual sorting left and right 
        pi = partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
# after the two parts are sorted both are combined and make a proper sorted array
quicksort(arr,0,len(arr)-1)
print(arr)
