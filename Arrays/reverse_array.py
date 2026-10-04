array=[1,2,3,4,5]

reverse_array=[]

for i in range(len(array)-1,-1,-1):
    reverse_array.append(array[i])

print(reverse_array)    
