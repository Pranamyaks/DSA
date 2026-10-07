'''
maximum number of 1s that appear continously next to each other
'''

array=[1,1,0,1,1,1,0,1]

max_count=0

count=0

for num in array:
    if num==1:
        count+=1
        if count>max_count:
            max_count=count
    elif num==0:
        count=0

print(max_count)        
    
        
