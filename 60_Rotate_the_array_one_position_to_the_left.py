nums = [10, 20, 30, 40, 50]
first = nums[0]

for i in range(len(nums) - 1):
    nums[i] = nums[i + 1]

nums[-1] = first
print(nums)
