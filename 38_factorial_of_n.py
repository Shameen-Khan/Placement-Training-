# Factorial of n

n = int(input("Enter a non-negative integer N: "))
if n < 0:
    print("Factorial is not defined for negative integers.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print("Factorial:", factorial)
