def radixsort(arr):
    max_value=max(arr)
    pos=1
    while max_value// pos>0:
        countersort(arr,pos)
        pos=pos*10
def countersort(arr,pos):
    n=len(arr)
    count=[0]*10
    output=[0]*n
    for i in arr:
        index=(i//pos)%10
        count[index]+=1
    for i in range(1,10):
        count[i]=count[i]+count[i-1]
    for i in reversed(arr):
        index=(i//pos)%10
        output[count[index]-1]=i
        count[index]=count[index]-1
    for i in range(n):
        arr[i]=output[i]
def printarray(arr):
    for i in arr:
        print(i,end=" ")
n=int(input("enter:"))
arr=[]
for i in range(n):
      arr.append(int(input("enter a number:")))
radixsort(arr)
printarray(arr)