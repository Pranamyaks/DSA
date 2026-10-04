numbers=list(map(int,input("Enter numbers:").split()))

new_list=[]

for num in numbers:
    if num!=0:
        new_list.append(num)

for num in numbers:
    if num==0:
        new_list.append(num)

print(new_list)                
