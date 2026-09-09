# Count number of digits

n = abs(int(input("Enter an integer: ")))
count = 0
if n == 0:
    count = 1
while n > 0:
    count += 1
    n //= 10
print("Number of digits:", count)
