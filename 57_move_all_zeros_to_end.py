nums = [0, 1, 0, 2, 0, 0, 0]
result = []
count = 0

for i in nums:
    if i == 0:
        count += 1
    else:
        result.append(i)
        
for i in range(count):
    result.append(0)
    
print(result)