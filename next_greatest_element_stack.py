arr = list(map(int,input().split()))
# to have the element if does not have a greatest element than it 
stack = []
# to store the greatest element if found else -1 in the same sized array
result = len(arr) * [-1]
for i in range(len(arr)):
    # when stack is not empty and current iterated element is greater than stack last element its poped and replaced 
    while stack and arr[i] > arr[stack[-1]]:
        idx = stack.pop()
        result[idx] = arr[i]
    stack.append(i)
# used aestrik to print with separated space without square bracket of list
print(*result)
