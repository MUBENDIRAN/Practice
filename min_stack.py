# we used class since we need to use multiple functions repeatedly
class Minstack:
    # this function defines the initialization of stack and min stack that should be stored
    def __init__(self,arr):
        self.st = []
        self.min_st = []
    # this function ensure element is added to both if minimum is found if not in any add there
    def push(self,x):
        self.st.append(x)
        if not self.min_st:
            self.min_st.append(x)
        else:
            self.min_st.append(min(x,self.min_st[-1]))
    # this function removes the last element since we need the minimum
    def pop(self):
        self.st.pop()
        self.min_st.pop()
    # this function removes last element of stack when the comparison of minimum ends
    def top(self):
        return self.st[-1]
    # this function gets the minimum value 
    def getMin(self):
        return self.min_st[-1]
# this gives input value for array and initialize to the class and gets the result 
arr = list(map(int,input().split()))
ms = Minstack(arr)
for x in arr:
    ms.push(x)
print(ms.top(),ms.getMin())       