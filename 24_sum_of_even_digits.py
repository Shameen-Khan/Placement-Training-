# Sum of even digits

n = abs(int(input("Enter an integer: ")))
result = 0
# Converting to text ensures that 0 is processed as one digit.
for character in str(n):
    digit = int(character)
    if digit % 2 == 0:
        result += digit
print("Sum of even digits:", result)
