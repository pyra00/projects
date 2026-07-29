# ==========================================
# Source File: SBA Activity 2 Practice _ .pdf
# ==========================================

def main():
    # ------------------------------------------
    # Exercise 1 (Practice)
    # ------------------------------------------
   
    # Store the provided 3x3 matrix.
    matrix = [
        [5, 10, 15],
        [20, 25, 30],
        [35, 40, 45]
    ]

    print(" Exercise 1 Output ")
   
    # Print every number using nested loops.
    for row in matrix:
        for value in row:
            print(value)

    print("\n")  # Spacer for clean terminal output

    # ------------------------------------------
    # Exercise 2 (Practice)
    # ------------------------------------------
   
    # Store the sales of three stores for four months.
    sales_matrix = [
        [1200, 1500, 1800, 2000],
        [1400, 1600, 1900, 2200],
        [1300, 1700, 2100, 2300]
    ]

    # Calculate the grand total of all sales.
    grand_total = 0

    # Traverse all values using a running total (+= value).
    for row in sales_matrix:
        for value in row:
            grand_total += value

    print("--- Exercise 2 Output ---")
    print(f"Grand Total of all sales: {grand_total}")

if __name__ == "__main__":
    main()
