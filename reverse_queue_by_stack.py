from collections import deque
arr = list(map(int,input().split()))
arr = q
q = deque()
def reverseQueue(q):
    st =  []

    while q:
        value = q.pop()
        st.append(value)

    while st:
        value = st.pop()
        q.append(value)

reverseQueue(q)