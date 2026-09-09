# Count odd digits

n = abs(int(input("Enter an integer: ")))
result = 0
# Converting to text ensures that 0 is processed as one digit.
for character in str(n):
    digit = int(character)
    if digit % 2 == 1:
        result += 1
print("Count of odd digits:", result)
