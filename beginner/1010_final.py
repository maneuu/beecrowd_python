linha1 = input().split()
linha2 = input().split()

item1_quantity = int(linha1[1])
item1_unit_price = float(linha1[2])

item2_quantity = int(linha2[1])
item2_unit_price = float(linha2[2])

total_cost = (item1_quantity * item1_unit_price) + (item2_quantity * item2_unit_price)

print(f"VALOR A PAGAR: R$ {total_cost:.2f}")