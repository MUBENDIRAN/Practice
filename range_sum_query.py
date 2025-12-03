n = int(input())
arr = list(map(int,input().split()))
# create a similar size of n list to store the values of sum
prefix = [0]*n
# since first element will be same no change so added directly to prefix
prefix[0] = arr[0]
# As we added the first element we start from second index 1
for i in range(1,n):
    # we add the current iteration with previously stored value in prefix
    prefix[i] = prefix[i-1] + arr[i]
# This gets the number of queries
q = int(input())
for _ in range(q):
    # Receive the range of values to be query sum 
    L,R = map(int,input().split())
    # if the initial value is 0 then the loop before goes upto the query and pick the range sum 
    if L == 0:
        print(prefix[R])
    # IF the initial and final are non zeros using the below formula last - (first - 1) we the sum of the range sum query
    else:
        print(prefix[R] - prefix[L-1])
