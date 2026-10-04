numbers=list(map(int,input("Enter numbers:").split()))
print(numbers)

flag=0
for i in range(len(numbers)-1):
    if numbers[i] < numbers[i+1]:
        flag=1
    else:
        flag=0

if flag:
    print("Array is sorted")

else:
    print("Array is not sorted")               
