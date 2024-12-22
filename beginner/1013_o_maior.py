valores = input("insira os valores: ").split()
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

ab = (a + b + abs(a-b))/2
maior_final = int((ab + c + abs(ab - c))/2)

print(f"{maior_final} eh o maior")