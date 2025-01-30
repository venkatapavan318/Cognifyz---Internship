# Number of rows for the pyramid
rows = int(input("Enter the number of rows: "))

# Outer loop for rows
for i in range(1, rows + 1):
    # Inner loop for spaces (for alignment)
    for space in range(rows - i):
        print(" ", end="")
    
    # Inner loop for numbers
    for num in range(1, i + 1):
        print(num, end=" ")
    
    # Move to the next line after each row
    print()
