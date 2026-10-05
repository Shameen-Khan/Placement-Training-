num = [1, -2, 3, -4, -5, 6]
result = []

for i in num:
    if i < 0:
        result.append(i)

for i in num:
    if i > 0:
        result.append(i)
print(result)
