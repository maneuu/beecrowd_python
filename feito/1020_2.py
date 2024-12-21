idade_dias = int(input(">> "))

ano = mes = dia = 0


if idade_dias > 360 and idade_dias < 365:
    mes += int(idade_dias / 30)
    idade_dias = 0
else:
    ano += int(idade_dias / 365)
    idade_dias = idade_dias - (365 * ano)
        
    mes += int(idade_dias / 30)
    idade_dias = idade_dias - (30 * mes)

    dia += idade_dias

print(f'''{ano} ano(s)
{mes} mes(es)
{dia} dia(s)''')