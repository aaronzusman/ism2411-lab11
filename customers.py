
# Reflection 1:
# I would use .get() when a dictionary value could be missing, because it
# allows the program to continue with a default value. I would use the bracket
# notation for the times that I know the key exists and need its value. 

# Reflection 2:
# This pattern reminds me of using SUMIF in Excel to add values based on
# categories. Python can be way more helpful for large datasets because it can
# automatically process many records and create summaries with loops.

# EXERCISE 1 - One Customer

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1200
}

print("EXERCISE 1")
print("Name:", customer["name"])
print("Email:", customer["email"])
print("Tier:", customer["tier"])
print("YTD Spend:", customer["ytd_spend"])
print("Full customer dictionary:", customer)


# EXERCISE 2 - Update and Add

print("\nEXERCISE 2")

customer["phone"] = "813-555-1234"
print("After adding phone:", customer)

customer["tier"] = "platinum"
print("After updating tier:", customer)

del customer["email"]
print("After deleting email:", customer)


# EXERCISE 3 - Safe Lookup

print("\nEXERCISE 3")

email = customer.get("email", "no email on file")
print("Email using get():", email)

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist in the dictionary")


# EXERCISE 4 - Iterate

print("\nEXERCISE 4")

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only returns the dictionary keys,
# not both the keys and their values.


# EXERCISE 5 - Lookup Table

print("\nEXERCISE 5")

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]
discount_rate = tier_discounts.get(tier, 0)
purchase_price = 200
final_price = purchase_price * (1 - discount_rate)

print("Tier:", tier)
print("Discount rate:", discount_rate * 100, "%")
print("Final price: $", round(final_price, 2))


# EXERCISE 6 - List of Dictionaries

print("\nEXERCISE 6")

customers = [
    {"name": "Alice", "tier": "gold"},
    {"name": "Bob", "tier": "silver"},
    {"name": "Charlie", "tier": "bronze"}
]

for customer_info in customers:
    name = customer_info["name"]
    tier = customer_info["tier"]
    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount_rate

    print(
        f"{name} | Tier: {tier} | "
        f"Discount: ${discount_amount:.2f}"
    )


# EXERCISE 7 - Nested Catalog

print("\nEXERCISE 7")

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(
            f"LOW STOCK: {product} "
            f"(Stock: {details['stock']})"
        )


# EXERCISE 8 - Sales by Region

print("\nEXERCISE 8")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_summary[region] = sales_summary.get(region, 0) + amount

for region in sorted(sales_summary):
    print(f"{region}: ${sales_summary[region]}")
