# Check leap year

year = int(input("Enter a positive year: "))
if year <= 0:
    print("Please enter a positive year.")
elif year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")
