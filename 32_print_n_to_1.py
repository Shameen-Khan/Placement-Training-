# Print n to 1

n = int(input("Enter a positive integer N: "))
if n < 1:
    print("Please enter a positive integer.")
else:
    for i in range(n, 0, -1):
        print(i, end=" ")
    print()
