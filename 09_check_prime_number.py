# Check prime number

n = int(input("Enter an integer: "))
is_prime = n >= 2
divisor = 2
while divisor * divisor <= n:
    if n % divisor == 0:
        is_prime = False
        break
    divisor += 1
if is_prime:
    print("Prime number")
else:
    print("Not a prime number")
