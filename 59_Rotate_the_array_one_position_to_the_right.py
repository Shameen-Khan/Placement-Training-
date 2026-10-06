nums = [10, 20, 30, 40, 50]
last = nums[-1]

for i in range(len(nums) - 1, 0, -1):
    nums[i] = nums[i - 1]

nums[0] = last

print(nums)
