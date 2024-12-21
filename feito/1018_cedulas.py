valor_input = int(input(">> "))

valor = valor_input

# notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.
nota100 = nota50 = nota20 = nota10 = nota5 = nota2 = nota1= 0

while valor != 0:
    if valor >= 100:
        nota100 +=1
        valor -= 100
    elif valor >= 50:
        nota50 += 1
        valor -= 50
    elif valor >= 20:
        nota20 += 1
        valor -= 20
    elif valor >= 10:
        nota10 += 1
        valor -= 10
    elif valor >= 5:
        nota5 += 1
        valor -= 5
    elif valor >= 2:
        nota2 += 1
        valor -= 2
    elif valor >= 1:
        nota1 += 1
        valor -= 1

print(f'''{valor_input}
{nota100} nota(s) de R$ 100,00
{nota50} nota(s) de R$ 50,00
{nota20} nota(s) de R$ 20,00
{nota10} nota(s) de R$ 10,00
{nota5} nota(s) de R$ 5,00
{nota2} nota(s) de R$ 2,00
{nota1} nota(s) de R$ 1,00
''')