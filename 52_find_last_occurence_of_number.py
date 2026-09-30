num = [2, 4, 6, 8, 10]
n = int(input("Enter a number :"))
for i in range(len(num)):
    if num[i] == n:
        print(f"First Occurence of {n} is at index {i}")
        break
else:
    print("Number does not exist") 
