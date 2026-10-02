nums = [1, 3, 2, 5, 4, 7, 8, 5]
count = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        count += 1

print("Increasing adjacent pairs:", count)
