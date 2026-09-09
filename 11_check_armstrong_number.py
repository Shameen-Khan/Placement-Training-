# Check armstrong number

# Sum of each digit raised to the number of digits equals the number.
n = int(input("Enter a non-negative integer: "))
if n < 0:
    print("Please enter a non-negative integer.")
else:
    power = len(str(n))
    total = 0
    for digit in str(n):
        total += int(digit) ** power
    if total == n:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")
