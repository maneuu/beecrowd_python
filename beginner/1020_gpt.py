idade_dias = int(input(">> "))

ano = idade_dias // 365  # Calcula os anos inteiros
idade_dias %= 365        # Calcula o restante em dias após subtrair os anos

mes = idade_dias // 30   # Calcula os meses inteiros
dia = idade_dias % 30    # Calcula os dias restantes

print(f'''{ano} ano(s)
{mes} mes(es)
{dia} dia(s)''')
