num = [2, 4, 6, 8]
n = int(input("Enter a number:"))
last = -1

for i in range(len(num)):
    if num[i] == n:
        last = i
        print(f"The Last Occurence of the number {n} is at index {last}")
else:
    print("Number does not exist")
