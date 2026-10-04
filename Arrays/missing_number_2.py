arr=list(map(int,input("enter number:").split()))

n=len(arr)+1

total=n*(n+1)//2

sum=0

for i in arr:
    sum+=i

missing=total-sum

print(missing)
