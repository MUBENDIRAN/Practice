from collections import dequeue
def reverseQueue(q):
    st =  []

    while q:
        value = q.pop()
        st.append(value)

    while st:
        value = st.pop()
        q.append(value)