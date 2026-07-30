# 1. Create the salary table.
salaries = [
    [5000, 5200, 5100],
    [4800, 4950, 5050],
    [6000, 6100, 6200]
]

# 2. Assume the first salary is both the highest and lowest.
highest = salaries[0][0]
lowest = salaries[0][0]

# 3. Loop through each department.
for row in salaries:

    # 4. Loop through each employee salary.
    for salary in row:

        # 5. Display the salary.
        print(f"${salary}", end="\t")

        # 6. Is this the highest salary?
        if salary > highest:
            highest = salary

        # 7. Is this the lowest salary?
        if salary < lowest:
            lowest = salary

    # 8. Move to the next department.
    print()

# 9. Display the highest salary.
print("\nHighest Salary = $", highest)

# 10. Display the lowest salary.
print("Lowest Salary = $", lowest)
