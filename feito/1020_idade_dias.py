idade_dias = int(input(">> "))

ano = mes = dia = 0

if idade_dias >= 365:
    ano += int(idade_dias / 365)
    idade_dias = idade_dias - (365 * ano)
if idade_dias > 360 and idade_dias < 365:
    mes += int(idade_dias / 30)
    idade_dias = 0
if idade_dias >= 30:
    mes += int(idade_dias / 30)
    idade_dias = idade_dias - (30 * mes)
if idade_dias > 0:
    dia += idade_dias
    idade_dias = 0

print(f'''{ano} ano(s)
{mes} mes(es)
{dia} dia(s)''')