# Count occurrence of a digit

n = abs(int(input("Enter an integer: ")))
target = int(input("Enter the digit to count (0-9): "))
if target < 0 or target > 9:
    print("Please enter a single digit from 0 to 9.")
else:
    count = 0
    for character in str(n):
        if int(character) == target:
            count += 1
    print("Occurrences:", count)
