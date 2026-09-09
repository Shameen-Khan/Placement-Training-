# Check strong number

# Sum of the factorials of the digits equals the number (example: 145).
n = int(input("Enter a non-negative integer: "))
if n < 0:
    print("Please enter a non-negative integer.")
else:
    total = 0
    for digit in str(n):
        factorial = 1
        for i in range(1, int(digit) + 1):
            factorial *= i
        total += factorial
    if total == n:
        print("Strong number")
    else:
        print("Not a strong number")
