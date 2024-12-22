valores1 = input().split()
valores2 = input().split()

x1 = float(valores1[0])
y1 = float(valores1[1])

x2 = float(valores2[0])
y2 = float(valores2[1])

distancia =( (x2 - x1) ** 2 + (y2 - y1) ** 2 ) ** 0.5
print(f"{distancia:.4f}")