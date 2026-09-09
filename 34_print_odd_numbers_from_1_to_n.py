# Print odd numbers from 1 to n

n = int(input("Enter a positive integer N: "))
if n < 1:
    print("Please enter a positive integer.")
else:
    for i in range(1, n + 1, 2):
        print(i, end=" ")
    print()
