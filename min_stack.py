arr = list(map(int,input().split()))
class Minstack:
    def __init__(self,arr):
        self.st = []
        self.min_st = []

    def push(self,x):
        self.st.append(x)
        if not self.min_st:
            self.min_st.append(x)
        else:
            self.min_st.append(min(x,self.min_st[-1]))

    def pop(self):
        self.st.pop()
        self.min_st.pop()

    def top(self):
        return self.st[-1]

    def getMin(self):
        return self.min_st[-1]
        