numbers=[11,22,11,22,33,44]

seen=set()
duplicates=set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(list(duplicates))            
