from collections import deque
arr = list(map(int,input().split()))
q = deque(arr)
def reverseQueue(q):
    st =  []

    while q:
        value = q.popleft()
        st.append(value)

    while st:
        value = st.pop()
        q.append(value)

reverseQueue(q)
print(*q)