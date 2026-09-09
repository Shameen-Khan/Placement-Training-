# Count multiples of 3 from 1 to n

n = int(input("Enter a non-negative integer N: "))
if n < 0:
    print("Please enter a non-negative integer.")
else:
    count = 0
    for i in range(3, n + 1, 3):
        count += 1
    print("Count of multiples of 3:", count)
