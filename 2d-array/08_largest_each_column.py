# 8. Largest each column

# Enter positive dimensions and space-separated integer rows.
rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))
if rows <= 0 or cols <= 0:
    raise SystemExit("Rows and columns must be positive.")

matrix = []
for i in range(rows):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    if len(row) != cols:
        raise SystemExit(f"Each row must contain {cols} numbers.")
    matrix.append(row)

for j in range(cols):
    largest = matrix[0][j]
    for i in range(rows):
        if matrix[i][j] > largest:
            largest = matrix[i][j]
    print("Largest in column", j + 1, ":", largest)
