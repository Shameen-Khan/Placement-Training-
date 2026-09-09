# Check perfect number

# A positive number equal to the sum of its positive proper divisors.
n = int(input("Enter an integer: "))
total = 0
for divisor in range(1, n // 2 + 1):
    if n % divisor == 0:
        total += divisor
if n > 0 and total == n:
    print("Perfect number")
else:
    print("Not a perfect number")
