nums = [10, 20, 30, 40, 50]

p1 = int(input("Enter first position: "))
p2 = int(input("Enter second position: "))

if 1 <= p1 <= len(nums) and 1 <= p2 <= len(nums):
    nums[p1 - 1], nums[p2 - 1] = nums[p2 - 1], nums[p1 - 1]
    print(nums)
else:
    print("Invalid positions")
