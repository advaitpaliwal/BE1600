state_tax_rate = 0.04
county_tax_rate = 0.02

total_sales = float(input("Enter the total sales for the month: "))
state_tax = state_tax_rate * total_sales
county_tax = county_tax_rate * total_sales
print(f"Monthly sales: ${total_sales}")
print(f"State tax: ${state_tax}")
print(f"County tax: ${county_tax}")
print(f"Total tax: ${state_tax+county_tax}")
