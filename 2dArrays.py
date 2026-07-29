# Program 1_Create_2D_Array.py
# Create a 2D list and print the list structure.
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print(numbers)

# Program 2_Print_Rows.py
# Print each row of the 2D list separately.
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print(numbers[0])
print(numbers[1])
print(numbers[2])

# Program 3_Access_Elements.py
# Access and print specific elements from the 2D list.
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print(numbers[0][0])
print(numbers[0][2])
print(numbers[1][1])
print(numbers[2][0])

# Program 4_Modify_Value.py
# Modify a value inside the 2D list and print the result.
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
numbers[1][1] = 500
print(numbers)

# Program 5_Number_of_Rows.py
# Print the number of rows in the 2D list.
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print("Rows =", len(numbers))

# Program 6_Number_of_Columns.py
# Print the number of columns in the first row of the 2D list.
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print("Columns =", len(numbers[0]))

# Program 7_Print_Each_Row.py
# Print each row in the 2D list using a loop.
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
for row in numbers:
    print(row)

# Program 8_Nested_Loops.py
# Print every value in the 2D list using nested loops.
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
for row in numbers:
    for value in row:
        print(value)

# Program 9_Table_Format.py
# Print values in a table format with tab separation.
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
for row in numbers:
    for value in row:
        print(value, end="\t")
    print()

# Program 10_Total.py
# Calculate and print the sum of all values in the 2D list.
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
total = 0
for row in numbers:
    for value in row:
        total += value
print("Total =", total)

# Program 11_Find_Maximum.py
# Find and print the largest value in the 2D list.
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
largest = numbers[0][0]
for row in numbers:
    for value in row:
        if value > largest:
            largest = value
print("Largest =", largest)

# Program 12_Search.py
# Search for a target value in the 2D list and print whether it was found.
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
target = 50
found = False
for row in numbers:
    for value in row:
        if value == target:
            found = True
if found:
    print("Found")
else:
    print("Not Found")

# Program 13_Student_Scores.py
# Compute and print total and average score for each student.
students = [
    ["Alice", 85, 90, 88],
    ["Bob", 75, 82, 91],
    ["Charlie", 95, 89, 94]
]
for student in students:
    name = student[0]
    total = student[1] + student[2] + student[3]
    average = total / 3
    print(name)
    print("Total:", total)
    print("Average:", average)
    print()
