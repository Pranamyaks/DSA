arr=list(map(int,input("enter numbers:").split()))

print(arr)

for i in range(1,len(arr)+1):
    if i not in arr:
        print(i)
