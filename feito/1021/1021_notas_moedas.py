valor = float(input('Valor: '))


nota_100 = 0
nota_50 = 0
nota_20 = 0
nota_10 = 0
nota_5 = 0
nota_2 = 0
moeda_1 = 0
moeda_05 = 0
moeda_025 = 0
moeda_01 = 0
moeda_005 = 0
moeda_001 = 0

while True:
    if valor >= 100:
        nota_100 += 1
        valor -= 100
    elif valor >= 50:
        nota_50 += 1
        valor -= 50
    elif valor >= 20:
        nota_20 += 1
        valor -= 20
    elif valor >= 10:
        nota_10 += 1
        valor -= 10
    elif valor >= 5:
        nota_5 += 1
        valor -= 5
    elif valor >= 2:
        nota_2 += 1
        valor -= 2
    elif valor >= 1:
        moeda_1 += 1
        valor -= 1
    elif valor >= 0.5:
        moeda_05 += 1
        valor -= 0.5
    elif valor >= 0.25:
        moeda_025 += 1
        valor -= 0.25
    elif valor >= 0.10:
        moeda_01 += 1
        valor -= 0.1
    elif valor >= 0.05:
        moeda_005 += 1
        valor -= 0.05
    elif valor >= 0.01:
        moeda_001 += 1
        valor -= 0.01
    elif valor < 0.01:
        break

print(f'''NOTAS:
{nota_100} nota(s) de R$ 100.00
{nota_50} nota(s) de R$ 50.00
{nota_20} nota(s) de R$ 20.00
{nota_10} nota(s) de R$ 10.00
{nota_5} nota(s) de R$ 5.00
{nota_2} nota(s) de R$ 2.00
MOEDAS:
{moeda_1} moeda(s) de R$ 1.00
{moeda_05} moeda(s) de R$ 0.50
{moeda_025} moeda(s) de R$ 0.25
{moeda_01} moeda(s) de R$ 0.10
{moeda_005} moeda(s) de R$ 0.05
{moeda_001} moeda(s) de R$ 0.01''')