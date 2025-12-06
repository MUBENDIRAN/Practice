# we used built in library for easy access of queue
from collections import deque
arr = list(map(int,input().split()))
# to give the input to q the queue
q = deque(arr)
# we used function since we use same parameter for different operations
def reverseQueue(q):
    # this stack is to store the reverse since stack is LIFO
    st =  []
    # while q is not empty all values are removed and given to stack for reversing
    while q:
        value = q.popleft()
        st.append(value)
    # when stack has values ( reversed version of queue) its gets removed and again given to queue so queue gets its reversed version
    while st:
        value = st.pop()
        q.append(value)
# we get the output and printed with space 
reverseQueue(q)
print(*q)