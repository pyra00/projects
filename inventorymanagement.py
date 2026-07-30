# Step 1 - Create a 2D List

inventory = [
    [15, 22, 18],
    [30, 12, 25],
    [10, 28, 35]
]

print(inventory)
# Step 2 - Print One Row

inventory = [
    [15, 22, 18],
    [30, 12, 25],
    [10, 28, 35]
]

print(inventory[0])
# Step 3 - Print One Item

inventory = [
    [15, 22, 18],
    [30, 12, 25],
    [10, 28, 35]
]

print(inventory[0][1])
# Step 4 - Loop Through Each Row

inventory = [
    [15, 22, 18],
    [30, 12, 25],
    [10, 28, 35]
]

for row in inventory:
    print(row)
# Step 5 - Loop Through Every Item

inventory = [
    [15, 22, 18],
    [30, 12, 25],
    [10, 28, 35]
]

for row in inventory:

    for item in row:
        print(item)
# Step 6 - Display Items Like a Table

inventory = [
    [15, 22, 18],
    [30, 12, 25],
    [10, 28, 35]
]

for row in inventory:

    for item in row:
        print(item, end="\t")

    print()
# Step 7 - Create a Total Variable

inventory = [
    [15, 22, 18],
    [30, 12, 25],
    [10, 28, 35]
]

total = 0

print(total)
# Step 8 - Calculate Total Inventory

inventory = [
    [15, 22, 18],
    [30, 12, 25],
    [10, 28, 35]
]

total = 0

for row in inventory:

    for item in row:

        total += item

print("Total Inventory =", total)
# Step 8 - Calculate Total Inventory

inventory = [
    [15, 22, 18],
    [30, 12, 25],
    [10, 28, 35]
]

total = 0

for row in inventory:

    for item in row:

        total += item

print("Total Inventory =", total)
# Step 9 - Display and Add

inventory = [
    [15, 22, 18],
    [30, 12, 25],
    [10, 28, 35]
]

total = 0

for row in inventory:

    for item in row:

        print(item, end="\t")
        total += item

    print()

print("\nTotal Inventory =", total)
# Step 10 - Create a Counter

inventory = [
    [15, 22, 18],
    [30, 12, 25],
    [10, 28, 35]
]

count = 0

print(count)
# Step 12 - Total and Counter Together

inventory = [
    [15, 22, 18],
    [30, 12, 25],
    [10, 28, 35]
]

total = 0
count = 0

