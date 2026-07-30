salaries = [
    [5000, 5200, 5100],
    [4800, 4950, 5050],
    [6000, 6100, 6200]
]

# 1. Display the first department.
print(salaries[0])
print(salaries[0][0])
for row in salaries:

    # 2. Display one department.
    print(row)
for row in salaries:

    # 2. Loop through each salary.
    for salary in row:

        # 3. Display the salary.
        print(salary)
# 1. Loop through each department.
for row in salaries:

    # 2. Loop through each salary.
    for salary in row:

        # 3. Display each salary on the same line.
        print(salary, end="\t")

    # 4. Move to the next row.
    print()
# 1. Loop through each department.
for row in salaries:

    # 2. Loop through each salary.
    for salary in row:

        # 3. Display salary with a dollar sign.
        print(f"${salary}", end="\t")

    # 4. Move to the next row.
    print()
salaries = [
    [5000, 5200, 5100],
    [4800, 4950, 5050],
    [6000, 6100, 6200]
]

# 1. Assume the first salary is the highest.
highest = salaries[0][0]

# 2. Display it.
print(highest)
# 1. Assume the first salary is the highest.
highest = salaries[0][0]

# 2. Check every salary.
for row in salaries:

    for salary in row:

        # 3. Is this salary larger?
        if salary > highest:

            # 4. Save the new highest salary.
            highest = salary

# 5. Display the result.
print("Highest Salary =", highest)
salaries = [
    [5000, 5200, 5100],
    [4800, 4950, 5050],
    [6000, 6100, 6200]
]

# 1. Assume the first salary is the lowest.
lowest = salaries[0][0]

# 2. Display it.
print(lowest)
# 1. Assume the first salary is the lowest.
lowest = salaries[0][0]

# 2. Check every salary.
for row in salaries:

    for salary in row:

        # 3. Is this salary smaller?
        if salary < lowest:

            # 4. Save the new lowest salary.
            lowest = salary

# 5. Display the result.
print("Lowest Salary =", lowest)
