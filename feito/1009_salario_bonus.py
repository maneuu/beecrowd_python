seller_name = input("Enter the seller's name: ")
fixed_salary = float(input("Enter the fixed salary: "))
total_sales = float(input("Enter the total sales: "))

commission_rate = 0.15
commission = total_sales * commission_rate
total_salary = fixed_salary + commission

print(f"TOTAL = R$ {total_salary:.2f}")