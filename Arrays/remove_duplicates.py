numbers=[11,22,11,22,33,44]

unique_list=[]

for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print(unique_list)        
