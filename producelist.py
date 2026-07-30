# Step 8 - Complete Program

prices = [
    [12.99, 8.50, 15.75],
    [5.99, 9.49, 14.99],
    [20.00, 18.50, 7.25]
]

# Assume the first price is both the highest and lowest.
highest = prices[0][0]
lowest = prices[0][0]

# Store the total value.
total = 0

# Loop through each row.
for row in prices:

    # Loop through each price.
    for price in row:

        # Display the formatted price.
        print(f"${price:.2f}", end="\t")

        # Add to the total.
        total += price

        # Update the highest price.
        if price > highest:
            highest = price

        # Update the lowest price.
        if price < lowest:
            lowest = price

    print()

print("\nTotal Value = $", round(total, 2))
print("Most Expensive = $", highest)
print("Cheapest = $", lowest)
