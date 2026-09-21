a = [10, 20, 30, 40, 50]

average = sum(a) / len(a)

count = 0

for x in a:
    if x < average:
        count += 1

print("Average =", average)
print("Count =", count)