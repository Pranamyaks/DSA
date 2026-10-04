arr=list(map(int,input("Enter numbers:").split()))
k=int(input("Enter the rotate position:"))

n=len(arr)
k=k%n

#reverse the whole array
i=0
j=n-1

while i<j:
    arr[i],arr[j]=arr[j],arr[i]
    i+=1
    j-=1

#reverse the first k elements
i=0
j=k-1

while i<j:
    arr[i],arr[j]=arr[j],arr[i]
    i+=1
    j-=1

#reverse the remaining elements
i=k
j=n-1

while i<j:
    arr[i],arr[j]=arr[j],arr[i]
    i+=1
    j-=1

print(arr)    
