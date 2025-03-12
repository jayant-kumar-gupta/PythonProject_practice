import os


def insert():
    """Add sales records to the data file with correct formatting."""
    while True:
        product = input("Enter product name: ").strip().lower()  # Case normalization
        try:
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per unit: "))
        except ValueError:
            print("Invalid input! Use numbers for quantity/price.")
            continue

        # Write to file in correct format: Product,Quantity,Price
        with open("sales_data.csv", "a") as f:
            f.write(f"{product},{quantity},{price}\n")
        print("Record added successfully!")

        if input("Add another? (y/n): ").lower() != 'y':
            break


def view():
    """Generate sales report from data file."""
    try:
        with open("sales_data.csv", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Error: No sales data found!")
        return

    # Aggregate data
    sales = {}
    for line in lines:
        try:
            product, qty, price = line.strip().split(',')
            product = product.lower().strip()  # Case normalization
            qty = int(qty)
            price = float(price)
        except ValueError:
            print(f"Skipping invalid data: {line.strip()}")
            continue

        total = qty * price
        if product in sales:
            sales[product] += total
        else:
            sales[product] = total

    # Generate report
    if not sales:
        print("No valid data to generate report.")
        return

    # Sort products alphabetically
    sorted_products = sorted(sales.items())
    overall_total = sum(sales.values())
    max_sales = max(sales.values())
    best_sellers = [p for p, t in sorted_products if t == max_sales]

    # Format output
    print("\nSales Report:")
    print("------------")
    for product, total in sorted_products:
        print(f"{product.title()}: ${total:.2f}")
    print("------------")
    print(f"Total Sales: ${overall_total:.2f}")
    print(f"Best Selling Product(s): {', '.join([p.title() for p in best_sellers])}\n")


def main():
    while True:
        print("\n1. Add Sale\n2. Generate Report\n3. Exit")
        choice = input("Enter choice (1-3): ")

        if choice == '1':
            insert()
        elif choice == '2':
            view()
        elif choice == '3':
            # Cleanup files
            if os.path.exists("sales_data.csv"):
                os.remove("sales_data.csv")
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()