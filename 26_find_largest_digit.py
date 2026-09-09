# Find largest digit

n = abs(int(input("Enter an integer: ")))
result = n % 10
while n > 0:
    digit = n % 10
    if digit > result:
        result = digit
    n //= 10
print("Largest digit:", result)
