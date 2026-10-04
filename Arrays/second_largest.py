numbers=[99,45,67,21,90]

largest=float('-inf')
second_largest=float('-inf')

for num in numbers:
    if num > largest:
        second_largest=largest
        largest=num

    elif num > second_largest and second_largest!=largest:
        second_largest=num
print(second_largest)            
