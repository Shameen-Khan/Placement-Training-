nums = [1, 3, 2, 5, 4, 7]

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        print(nums[i], end=" ")