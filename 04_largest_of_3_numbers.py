# Largest of 3 numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    result = a
elif b >= a and b >= c:
    result = b
else:
    result = c
print("Largest:", result)
