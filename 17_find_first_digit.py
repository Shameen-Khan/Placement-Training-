# Find first digit

n = abs(int(input("Enter an integer: ")))
while n >= 10:
    n //= 10
print("First digit:", n)
