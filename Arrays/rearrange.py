def rearrange(arr):
    pos=[]
    neg=[]

    for num in arr:
        if num>=0:
            pos.append(num)
        else:
            neg.append(num)

    result=[]

    for i in range(len(pos)):
        result.append(pos[i])
        result.append(neg[i])

    return result   

arr=[3,1,-2,-5,2,-4]
print(rearrange(arr)) 
                   
