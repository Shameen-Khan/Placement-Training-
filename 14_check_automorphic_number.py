# Check automorphic number

# The square ends with the original number (example: 25 * 25 = 625).
n = int(input("Enter a non-negative integer: "))
if n < 0:
    print("Please enter a non-negative integer.")
else:
    square = n * n
    if square % (10 ** len(str(n))) == n:
        print("Automorphic number")
    else:
        print("Not an automorphic number")
