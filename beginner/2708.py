veiculos = turistas = 0

while True:
    entrada = input().split()
    if entrada[0] == "ABEND":
        break
    n = int(entrada[1])
    if entrada[0] == "SALIDA":
        veiculos += 1
        turistas += n
    else:  # VUELTA
        veiculos -= 1
        turistas -= n

print(turistas)
print(veiculos)
