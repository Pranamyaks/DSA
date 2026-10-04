array=[1,2,3,4,5,6]

odd=0
even=0

for num in array:
    if num%2==0:
        even+=1
    else:
        odd+=1

print('Odd:',odd)
print('Even:',even)            
