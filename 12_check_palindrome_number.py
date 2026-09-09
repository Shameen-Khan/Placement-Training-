# Check palindrome number

n = int(input("Enter an integer: "))
# Negative numbers are not palindromes because of the minus sign.
original = str(n)
if original == original[::-1]:
    print("Palindrome number")
else:
    print("Not a palindrome number")
