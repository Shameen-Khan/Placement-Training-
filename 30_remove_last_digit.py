# Remove last digit

n = int(input("Enter an integer: "))
sign = -1 if n < 0 else 1
result = sign * (abs(n) // 10)
print("After removing last digit:", result)
