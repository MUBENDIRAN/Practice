num=int(input())
# since we need to count we make it to string orelse it will be considered as a single string
n=str(num)
#set count to zero since before loop the container must be empty
count=0
for a in n:
    count+=1
print(count)