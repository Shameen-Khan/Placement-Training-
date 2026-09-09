# Sum of odd numbers up to n

n = int(input("Enter a non-negative integer N: "))
if n < 0:
    print("Please enter a non-negative integer.")
else:
    total = 0
    for i in range(1, n + 1, 2):
        total += i
    print("Sum:", total)
