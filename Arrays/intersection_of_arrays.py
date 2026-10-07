arr1=[1,2,3,4,5]
arr2=[3,4,5,6]

seen=set(arr1)

for num in arr2:
    seen.add(num)

print(list(seen))     
