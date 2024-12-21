# Input: Reading details for item 1
item1_code = int(input("Enter the code for item 1: "))
item1_quantity = int(input("Enter the quantity for item 1: "))
item1_unit_price = float(input("Enter the unit price for item 1: "))

# Input: Reading details for item 2
item2_code = int(input("Enter the code for item 2: "))
item2_quantity = int(input("Enter the quantity for item 2: "))
item2_unit_price = float(input("Enter the unit price for item 2: "))

total_cost = (item1_quantity * item1_unit_price) + (item2_quantity * item2_unit_price)

print(f"VALOR A PAGAR: R$ {total_cost:.2f}")