# Check neon number

# Sum of the digits of the square equals the number (example: 9).
n = int(input("Enter a non-negative integer: "))
if n < 0:
    print("Please enter a non-negative integer.")
else:
    total = 0
    for digit in str(n * n):
        total += int(digit)
    if total == n:
        print("Neon number")
    else:
        print("Not a neon number")
